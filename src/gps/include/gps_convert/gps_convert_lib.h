#ifndef __LANE_DETECTOR_H__
#define __LANE_DETECTOR_H__

#include <time.h>
#include <iostream>
#include <math.h>
#include <opencv2/opencv.hpp>
#include <vector>
#include <ros/ros.h>
#include <cv_bridge/cv_bridge.h>
#include <image_transport/image_transport.h>
#include <sensor_msgs/image_encodings.h>
#include "std_msgs/Float64MultiArray.h"

using namespace cv;
using namespace std;

class lat_lon_point
{
    public:
        lat_lon_point(double lat,double lon);
        lat_lon_point();
        ~lat_lon_point();
        double latitude;
        double longitude;
};

class GPS
{

    public:
    GPS(ros::NodeHandle& nh,Mat src_map,lat_lon_point upper_left_point,lat_lon_point bottom_right_point);
    GPS(ros::NodeHandle& nh);

    ros::Rate loop_rate;

    void set_map_size(int width,int height);
    Point scale_to_image(lat_lon_point lat_lon);
    void drawCircle(lat_lon_point lat_lon);
    void run();

    Mat position_map;

    ~GPS();

    private:
    ros::Subscriber lat_lon_sub_;
    image_transport::ImageTransport it_;
    image_transport::Publisher gps_map_pub_;
    void lat_lon_callback(const std_msgs::Float64MultiArray::ConstPtr& msg);

    sensor_msgs::ImagePtr cv_convertTo_msg(string encode,Mat image);
    Mat map;
    int map_height;
    int map_width;
    lat_lon_point upper_left_point;
    lat_lon_point bottom_right_point;
    lat_lon_point current_point;

};


#endif
