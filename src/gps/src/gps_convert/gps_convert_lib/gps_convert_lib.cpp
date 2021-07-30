#include "gps_convert/gps_convert_lib.h"
#include "cv_bridge/cv_bridge.h"
#include "ros/message_traits.h"

lat_lon_point::lat_lon_point(double lat,double lon)
{
    this->latitude = lat;
    this->longitude = lon;
}

lat_lon_point::lat_lon_point(){}
lat_lon_point::~lat_lon_point(){}

GPS::GPS(ros::NodeHandle& nh)
:it_(nh)
    ,loop_rate(10)
{}

GPS::GPS(ros::NodeHandle& nh ,Mat src_map,lat_lon_point upper_left_point,lat_lon_point bottom_right_point)
    :it_(nh)
    ,loop_rate(10)
{
    this -> map = src_map.clone();
    this -> upper_left_point = upper_left_point;
    this -> bottom_right_point = bottom_right_point;
    this -> set_map_size(src_map.cols,src_map.rows);

    gps_map_pub_ = it_.advertise("gps_map/image", 1);
    this -> lat_lon_sub_ = nh.subscribe("lat_lon_topic",1000,&GPS::lat_lon_callback,this);
}
GPS::~GPS(){}
void GPS::set_map_size(int width,int height)
{
    this -> map_height = height;
    this -> map_width = width;

}
void GPS::lat_lon_callback(const std_msgs::Float64MultiArray::ConstPtr& msg)
{
  this-> current_point = lat_lon_point(msg->data.at(0),msg->data.at(1));

}
Point GPS::scale_to_image(lat_lon_point lat_lon)
{
    double y = ((lat_lon.latitude - this->bottom_right_point.latitude) * (this -> map_height - 0) / (this->upper_left_point.latitude - this->bottom_right_point.latitude )) + 0 ;
    y = map_height - y ;

    double x = ((lat_lon.longitude - this->upper_left_point.longitude) * (this -> map_width - 0) / (this->bottom_right_point.longitude - this-> upper_left_point.longitude)) + 0 ;


   return Point((int)x,(int)y);

}
void GPS::drawCircle(lat_lon_point lat_lon)
{
    Point point(scale_to_image(lat_lon));
    circle(this->position_map,point,5,Scalar(255,0,0),-1);
}
sensor_msgs::ImagePtr GPS::cv_convertTo_msg(string encode,Mat image)
{
   return cv_bridge::CvImage(std_msgs::Header(),encode,image).toImageMsg();
}
void GPS::run()
{
    this->position_map = this->map.clone();
    drawCircle(this->current_point);
    imshow("gps_map",this->position_map);
    gps_map_pub_.publish(cv_convertTo_msg("bgr8",this->position_map));
    waitKey(1);
}
