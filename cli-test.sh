#!/bin/bash

# Date/Time
./pa-cli.py --doe --year=2019
./pa-cli.py --cd_to_dn --civil_date="2/1/2019"
./pa-cli.py --gd_to_jd --greenwich_date="6/19.75/2009"
./pa-cli.py --jd_to_gd --jd=2455002.25
./pa-cli.py --ct_to_dh --civil_time="18:31:27"
./pa-cli.py --dh_to_ct --decimal_hours=18.52416667
./pa-cli.py --lct_to_ut --civil_date="7/1/2013" --civil_time="3:37:00" --zone_correction=4 --daylight_savings_time
./pa-cli.py --ut_to_lct --civil_date="6/30/2013" --ut="22:37:00" --zone_correction=4 --daylight_savings_time
./pa-cli.py --ut_to_gst --ut="14:36:51.67" --greenwich_date="4/22/1980"
./pa-cli.py --gst_to_ut --gst="4:40:5.23" --greenwich_date="4/22/1980"
./pa-cli.py --gst_to_lst --gst="4:40:5.23" --geo_long=-64
./pa-cli.py --lst_to_gst --lst="0:24:5.23" --geo_long=-64

# Coordinates
./pa-cli.py --a_to_dd --degrees=182 --minutes=31 --seconds=27
./pa-cli.py --dd_to_a --decimal_degrees=182.5241667
./pa-cli.py --ec_to_hc --ha_hr=5 --ha_min=51 --ha_sec=44 --decl_deg=23 --decl_min=13 --decl_sec=10 --geo_lat=52
./pa-cli.py --hc_to_ec --az_deg=283 --az_min=16 --az_sec=15.7 --alt_deg=19 --alt_min=20 --alt_sec=3.64 --geo_lat=52
./pa-cli.py --mean_obliq_ecliptic --greenwich_date="7/6/2009"
./pa-cli.py --ecl_c_to_equa_c --ecl_long_deg=139 --ecl_long_min=41 --ecl_long_sec=10 --ecl_lat_deg=4 --ecl_lat_min=52 --ecl_lat_sec=31 --greenwich_date="7/6/2009"
./pa-cli.py --equa_c_to_ecl_c --ra_hr=9 --ra_min=34 --ra_sec=53.4 --decl_deg=19 --decl_min=32 --decl_sec=8.52 --greenwich_date="7/6/2009"
./pa-cli.py --equa_c_to_gal_c --ra_hr=10 --ra_min=21 --ra_sec=0 --decl_deg=10 --decl_min=3 --decl_sec=11
./pa-cli.py --gal_c_to_equa_c --gal_long_deg=232 --gal_long_min=14 --gal_long_sec=52.38 --gal_lat_deg=51 --gal_lat_min=7 --gal_lat_sec=20.16
./pa-cli.py --ang_b_two_obj --ra_long1="5:13:31.7" --decl_lat1="-8:13:30" --ra_long2="6:44:13.4" --decl_lat2="-16:41:11" --h_or_d="H"
./pa-cli.py --rise_and_set --ra_hr=23 --ra_min=39 --ra_sec=20 --decl_deg=21 --decl_min=42 --decl_sec=0 --greenwich_date="8/24/2010" --geo_long=64 --geo_lat=30 --v_sh_deg=0.5667
./pa-cli.py --precession --ra_hr=9 --ra_min=10 --ra_sec=43 --decl_deg=14 --decl_min=23 --decl_sec=25 --epoch1="1/0.923/1950" --epoch2="6/1/1979"
./pa-cli.py --nutation --greenwich_date="9/1/1988"