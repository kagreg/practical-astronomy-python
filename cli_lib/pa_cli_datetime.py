import json
from dateutil.parser import parse
import lib.pa_datetime as PA_DT
import cli_lib.pa_cli_util as PA_UTIL

class CliDateTime:
	def __init__(self, args):
		self.args = args

	def eval_datetime(self):
		'''
		Determine if any date/time action args were passed.
		'''

		# Date of Easter
		if self.args.doe:
			if self.args.year == None:
				PA_UTIL.display_error("'year' argument is required.")
			else:
				self.doe_year(self.args.year)

		# Civil Date to Day Number
		if self.args.cd_to_dn:
			if self.args.civil_date == None:
				PA_UTIL.display_error("'civil_date' argument is required.")
			else:
				self.cd_to_dn(self.args.civil_date)

		# Greenwich Date to Julian Date
		if self.args.gd_to_jd:
			if self.args.greenwich_date == None:
				PA_UTIL.display_error("'greenwich_date' argument is required.")
			else:
				self.gd_to_jd(self.args.greenwich_date)

		# Julian Date to Greenwich Date
		if self.args.jd_to_gd:
			if self.args.jd == None:
				PA_UTIL.display_error("'jd' argument is required.")
			else:
				self.jd_to_gd(self.args.jd)

		# Civil Time to Decimal Hours
		if self.args.ct_to_dh:
			if self.args.civil_time == None:
				PA_UTIL.display_error("'civil_time' argument is required.")
			else:
				self.ct_to_dh(self.args.civil_time)

		# Decimal Hours to Civil Time
		if self.args.dh_to_ct:
			if self.args.decimal_hours == None:
				PA_UTIL.display_error("'decimal_hours' argument is required.")
			else:
				self.dh_to_ct(self.args.decimal_hours)

		# Local Civil Time to Universal Time
		if self.args.lct_to_ut:
			if self.args.civil_date == None:
				PA_UTIL.display_error("'civil_date', argument is required.")
			elif self.args.civil_time == None:
				PA_UTIL.display_error("'civil_time', argument is required.")
			elif self.args.zone_correction == None:
				PA_UTIL.display_error("'zone_correction', argument is required.")
			else:
				self.lct_to_ut(self.args.civil_date, self.args.civil_time, self.args.is_daylight_savings, self.args.zone_correction)

		# Universal Time to Local Civil Time
		if self.args.ut_to_lct:
			if self.args.civil_date == None:
				PA_UTIL.display_error("'civil_date', argument is required.")
			elif self.args.ut == None:
				PA_UTIL.display_error("'ut', argument is required.")
			elif self.args.zone_correction == None:
				PA_UTIL.display_error("'zone_correction', argument is required.")
			else:
				self.ut_to_lct(self.args.civil_date, self.args.ut, self.args.is_daylight_savings, self.args.zone_correction)

		# Universal Time to Greenwich Sidereal Time
		if self.args.ut_to_gst:
			if self.args.ut == None:
				PA_UTIL.display_error("'ut' argument is required.")
			elif self.args.greenwich_date == None:
				PA_UTIL.display_error("'greenwich_date' argument is required.")
			else:
				self.ut_to_gst(self.args.ut, self.args.greenwich_date)

		# Greenwich Sidereal Time to Universal Time
		if self.args.gst_to_ut:
			if self.args.gst == None:
				PA_UTIL.display_error("'gst' argument is required.")
			elif self.args.greenwich_date == None:
				PA_UTIL.display_error("'greenwich_date' argument is required.")
			else:
				self.gst_to_ut(self.args.gst, self.args.greenwich_date)

		# Greenwich Sidereal Time to Local Sidereal Time
		if self.args.gst_to_lst:
			if self.args.gst == None:
				PA_UTIL.display_error("'gst' argument is required.")
			elif self.args.geo_long == None:
				PA_UTIL.display_error("'geo_long' argument is required.")
			else:
				self.gst_to_lst(self.args.gst, self.args.geo_long)

		# Local Sidereal Time to Greenwich Sidereal Time
		if self.args.lst_to_gst:
			if self.args.lst == None:
				PA_UTIL.display_error("'lst' argument is required.")
			elif self.args.geo_long == None:
				PA_UTIL.display_error("'geo_long' argument is required.")
			else:
				self.lst_to_gst(self.args.lst, self.args.geo_long)

	def doe_year(self, year):
		'''
		Calculate date of Easter for a given year.
		'''
		easter_month,easter_day,easter_year = PA_DT.get_date_of_easter(year)
		easter_dict = dict(easterMonth=easter_month, easterDay=easter_day, easterYear=easter_year)

		print(json.dumps(easter_dict))

	def cd_to_dn(self, date_string):
		'''
		Convert civil date to day number.
		'''
		dt = parse(date_string)
		day_number = PA_DT.civil_date_to_day_number(dt.month, dt.day, dt.year)
		day_num_dict = dict(dayNumber=day_number)

		print(json.dumps(day_num_dict))

	def gd_to_jd(self, greenwich_date):
		'''
		Convert Greenwich date to Julian date.
		'''
		dt_split = greenwich_date.split("/")

		julian_date = PA_DT.greenwich_date_to_julian_date(float(dt_split[1]), int(dt_split[0]), int(dt_split[2]))
		julian_date_dict = dict(julianDate=julian_date)

		print(json.dumps(julian_date_dict))

	def jd_to_gd(self, julian_date):
		'''
		Convert Julian date to Greenwich date.
		'''
		day,month,year = PA_DT.julian_date_to_greenwich_date(julian_date)
		greenwich_date_dict = dict(greenwichDay=day, greenwichMonth=month, greenwichYear=year)

		print(json.dumps(greenwich_date_dict))

	def ct_to_dh(self, civil_time):
		'''
		Convert civil time to decimal hours.
		'''
		ct_split = civil_time.split(":")

		decimal_hours = PA_DT.civil_time_to_decimal_hours(int(ct_split[0]), int(ct_split[1]), int(ct_split[2]))
		decimal_hours = round(decimal_hours,8)
		decimal_hours_dict = dict(decimalHours=decimal_hours)

		print(json.dumps(decimal_hours_dict))

	def dh_to_ct(self, decimal_hours):
		'''
		Convert decimal hours to civil time.
		'''
		hours,minutes,seconds = PA_DT.decimal_hours_to_civil_time(decimal_hours)
		civil_time_dict = dict(civilTimeHours=hours, civilTimeMinutes=minutes, civilTimeSeconds=seconds)

		print(json.dumps(civil_time_dict))

	def lct_to_ut(self, civil_date, civil_time, is_dst, zone_correction):
		'''
		Convert local civil time to universal time.
		'''
		cd_split = civil_date.split("/")
		ct_split = civil_time.split(":")
		ut_hours,ut_minutes,ut_seconds,gw_day,gw_month,gw_year = PA_DT.local_civil_time_to_universal_time(int(ct_split[0]), int(ct_split[1]), int(ct_split[2]), is_dst, zone_correction, int(cd_split[1]), int(cd_split[0]), int(cd_split[2]))
		ut_dict = dict(utHours=ut_hours,utMinutes=ut_minutes,utSeconds=ut_seconds,greenwichDay=gw_day,greenwichMonth=gw_month,greenwichYear=gw_year)

		print(json.dumps(ut_dict))

	def ut_to_lct(self, civil_date, universal_time, is_dst, zone_correction):
		'''
		Convert universal time to local civil time.
		'''
		cd_split = civil_date.split("/")
		ut_split = universal_time.split(":")
		lct_hours,lct_minutes,lct_seconds,gw_day,gw_month,gw_year = PA_DT.universal_time_to_local_civil_time(int(ut_split[0]), int(ut_split[1]), int(ut_split[2]), is_dst, zone_correction, int(cd_split[1]), int(cd_split[0]), int(cd_split[2]))
		lct_dict = dict(lctHours=lct_hours,lctMinutes=lct_minutes,lctSeconds=lct_seconds,greenwichDay=gw_day,greenwichMonth=gw_month,greenwichYear=gw_year)

		print(json.dumps(lct_dict))

	def ut_to_gst(self, universal_time, greenwich_date):
		'''
		Convert Universal time to Greenwich sidereal time
		'''
		ut_split = universal_time.split(":")
		gd_split = greenwich_date.split("/")
		gst_hours,gst_minutes,gst_seconds = PA_DT.universal_time_to_greenwich_sidereal_time(int(ut_split[0]), int(ut_split[1]), float(ut_split[2]), int(gd_split[1]), int(gd_split[0]), int(gd_split[2]))
		gst_dict = dict(greenwichSiderealTimeHours=gst_hours, greenwichSiderealTimeMinutes=gst_minutes, greenwichSiderealTimeSeconds=gst_seconds)

		print(json.dumps(gst_dict))

	def gst_to_ut(self, greenwich_sidereal_time, greenwich_date):
		'''
		Convert Greenwich sidereal time to universal time
		'''
		gst_split = greenwich_sidereal_time.split(":")
		gd_split = greenwich_date.split("/")
		ut_hours,ut_minutes,ut_seconds,status_message = PA_DT.greenwich_sidereal_time_to_universal_time(int(gst_split[0]),int(gst_split[1]),float(gst_split[2]),int(gd_split[1]),int(gd_split[0]),int(gd_split[2]))
		ut_dict = dict(utHours=ut_hours,utMinutes=ut_minutes,utSeconds=ut_seconds,statusMessage=status_message)

		print(json.dumps(ut_dict))

	def gst_to_lst(self, greenwich_sidereal_time, geographical_longitude):
		'''
		Convert Greenwich sidereal time to local sidereal time
		'''
		gst_split = greenwich_sidereal_time.split(":")
		lst_hours,lst_minutes,lst_seconds = PA_DT.greenwich_sidereal_time_to_local_sidereal_time(int(gst_split[0]), int(gst_split[1]), float(gst_split[2]), geographical_longitude)
		lst_dict = dict(lstHours=lst_hours,lstMinutes=lst_minutes,lstSeconds=lst_seconds)

		print(json.dumps(lst_dict))

	def lst_to_gst(self, local_sidereal_time, geographical_longitude):
		'''
		Convert local sidereal time to Greenwich sidereal time
		'''
		lst_split = local_sidereal_time.split(":")
		gst_hours,gst_minutes,gst_seconds = PA_DT.local_sidereal_time_to_greenwich_sidereal_time(int(lst_split[0]),int(lst_split[1]),float(lst_split[2]),geographical_longitude)
		gst_dict = dict(gstHours=gst_hours,gstMinutes=gst_minutes,gstSeconds=gst_seconds)

		print(json.dumps(gst_dict))
