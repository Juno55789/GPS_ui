#include "ros/ros.h"
#include "std_msgs/Float64MultiArray.h"
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>


using namespace std;

int main(int argc,char** argv )
{
    ros::init(argc,argv,"gps_module");
    ros::NodeHandle nh;
    ros::Publisher lat_lon_pub = nh.advertise<std_msgs::Float64MultiArray>("lat_lon_topic",100);
    ros::Rate loop_rate(10);


//   lat_lon_point(22.733406123470473,120.27712211337128);
//   lat_lon_point(22.731268712453243,120.27864560801784);
//   lat_lon_point(22.732931146131484,120.28119907087616);
//   lat_lon_point(22.733148844283306,120.28343066866827);
//   lat_lon_point(22.73508832161072,120.28330192264178);
//   lat_lon_point(22.735800775760946,120.28353795702365);
//   lat_lon_point(22.73724546305811,120.27845248897812);
//   lat_lon_point(22.733782146024843,120.27725085927908);

    std_msgs::Float64MultiArray gps_data;
//==================Engineering College==============
    gps_data.data.push_back(22.733406123470473);
    gps_data.data.push_back(120.27712211337128);
//==================Engineering College==============
    gps_data.data.push_back(22.731268712453243);
    gps_data.data.push_back(120.27864560801784);
//==================Engineering College==============
    gps_data.data.push_back(22.732931146131484);
    gps_data.data.push_back(120.28119907087616);
//==================Engineering College==============
    gps_data.data.push_back(22.733148844283306);
    gps_data.data.push_back(120.28343066866827);
//==================Engineering College==============
    gps_data.data.push_back(22.73508832161072);
    gps_data.data.push_back(120.28330192264178);
//==================Engineering College==============
    gps_data.data.push_back(22.735800775760946);
    gps_data.data.push_back(120.28353795702365);
//==================Engineering College==============
    gps_data.data.push_back(22.73724546305811);
    gps_data.data.push_back(120.27845248897812);
//==================Engineering College==============
    gps_data.data.push_back(22.733782146024843);
    gps_data.data.push_back(120.27725085927908);



    int i = 0;
    while(ros::ok())
    {
        //ROS_INFO("plan");
        std_msgs::Float64MultiArray gps_msg;

        gps_msg.data.push_back(gps_data.data.at(2*i));
        gps_msg.data.push_back(gps_data.data.at(2*i+1));
        lat_lon_pub.publish(gps_msg);
        ROS_INFO("%d",i);
        ROS_INFO("( %4f , %4f ) : ",gps_msg.data.at(0),gps_msg.data.at(1));
        gps_msg.data.clear();

        ros::spinOnce();
        loop_rate.sleep();


        i++;
        if( 2*i+1 >= gps_data.data.size())
        {
            i = 0;
        }

        if( i > 100 )
            break;
    }

    return 0;


}
