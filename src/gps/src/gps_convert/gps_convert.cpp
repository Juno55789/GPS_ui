#include"gps_convert/gps_convert_lib.h"


int main(int argc,char** argv )
{
    ros::init(argc,argv,"gps_convert");
    ros::NodeHandle nh;

    Mat src = imread(argv[1],IMREAD_COLOR);

    if(src.empty())
    {
        ROS_INFO("Failed to load %s",argv[1]);
        return -1;
    }

    GPS gps(nh,src,lat_lon_point(22.7381,120.2750),lat_lon_point(22.7295,120.2908));

   while(ros::ok())
   {

//    ROS_INFO(" load %s",argv[1]);
    ros::spinOnce();
    gps.run();

    imshow("src",src);
   }
    return 0;


}
