from lyra.translator import Collection
from lyra.common import OneOrMore
from lyra.common import GeographicExtentType
from lyra.common import GeographicExtentMapType
from lyra.common import LabelType
from lyra.common import FreeEditionType
from lyra.common import UNREACHABLE
from typing import Union, Optional

"""
This code has been automatically generated
by Lyra. Specifically, the format for
this code can be found in

`lyra.translator.translate`
"""

class Collection_reanalysis_carra_pressure_levels(Collection):
    collection_name = 'reanalysis-carra-pressure-levels'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        domain = ['east_domain', 'west_domain'],
        leadtime_hour = ['1', '2', '3', '4', '5', '6', '9', '12', '15', '18', '21', '24', '27', '30'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        pressure_level = ['10', '20', '30', '50', '70', '100', '150', '200', '250', '300', '400', '500', '600', '700', '750', '800', '825', '850', '875', '900', '925', '950', '1000'],
        product_type = ['analysis', 'forecast'],
        time = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00'],
        variable = ['cloud_cover', 'geometric_vertical_velocity', 'geopotential', 'graupel', 'potential_vorticity', 'pseudo_adiabatic_potential_temperature', 'relative_humidity', 'specific_cloud_ice_water_content', 'specific_cloud_liquid_water_content', 'specific_cloud_rain_water_content', 'specific_cloud_snow_water_content', 'temperature', 'u_component_of_wind', 'v_component_of_wind'],
        year = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        data_format = ['grib', 'netcdf'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], domain: str, leadtime_hour: OneOrMore[str], month: OneOrMore[str], pressure_level: OneOrMore[str], product_type: str, time: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], data_format: str = 'grib'): 
        """
        Parameters
        ----------
        :param day:
        :type day: str

        **Valid values:**
        
        - 01

        
        - 02

        
        - 03

        
        - 04

        
        - 05

        
        - 06

        
        - 07

        
        - 08

        
        - 09

        
        - 10

        
        - 11

        
        - 12

        
        - 13

        
        - 14

        
        - 15

        
        - 16

        
        - 17

        
        - 18

        
        - 19

        
        - 20

        
        - 21

        
        - 22

        
        - 23

        
        - 24

        
        - 25

        
        - 26

        
        - 27

        
        - 28

        
        - 29

        
        - 30

        
        - 31

        ---

        :param domain:
        :type domain: str

        **Valid values:**
        
        - east_domain

        
        - west_domain

        ---

        :param leadtime_hour:
        :type leadtime_hour: str

        **Valid values:**
        
        - 1

        
        - 2

        
        - 3

        
        - 4

        
        - 5

        
        - 6

        
        - 9

        
        - 12

        
        - 15

        
        - 18

        
        - 21

        
        - 24

        
        - 27

        
        - 30

        ---

        :param month:
        :type month: str

        **Valid values:**
        
        - 01

        
        - 02

        
        - 03

        
        - 04

        
        - 05

        
        - 06

        
        - 07

        
        - 08

        
        - 09

        
        - 10

        
        - 11

        
        - 12

        ---

        :param pressure_level:
        :type pressure_level: str

        **Valid values:**
        
        - 10

        
        - 20

        
        - 30

        
        - 50

        
        - 70

        
        - 100

        
        - 150

        
        - 200

        
        - 250

        
        - 300

        
        - 400

        
        - 500

        
        - 600

        
        - 700

        
        - 750

        
        - 800

        
        - 825

        
        - 850

        
        - 875

        
        - 900

        
        - 925

        
        - 950

        
        - 1000

        ---

        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - analysis

        
        - forecast

        ---

        :param time:
        :type time: str

        **Valid values:**
        
        - 00:00

        
        - 03:00

        
        - 06:00

        
        - 09:00

        
        - 12:00

        
        - 15:00

        
        - 18:00

        
        - 21:00

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - cloud_cover

        
        - geometric_vertical_velocity

        
        - geopotential

        
        - graupel

        
        - potential_vorticity

        
        - pseudo_adiabatic_potential_temperature

        
        - relative_humidity

        
        - specific_cloud_ice_water_content

        
        - specific_cloud_liquid_water_content

        
        - specific_cloud_rain_water_content

        
        - specific_cloud_snow_water_content

        
        - temperature

        
        - u_component_of_wind

        
        - v_component_of_wind

        ---

        :param year:
        :type year: str

        **Valid values:**
        
        - 1990

        
        - 1991

        
        - 1992

        
        - 1993

        
        - 1994

        
        - 1995

        
        - 1996

        
        - 1997

        
        - 1998

        
        - 1999

        
        - 2000

        
        - 2001

        
        - 2002

        
        - 2003

        
        - 2004

        
        - 2005

        
        - 2006

        
        - 2007

        
        - 2008

        
        - 2009

        
        - 2010

        
        - 2011

        
        - 2012

        
        - 2013

        
        - 2014

        
        - 2015

        
        - 2016

        
        - 2017

        
        - 2018

        
        - 2019

        
        - 2020

        
        - 2021

        
        - 2022

        
        - 2023

        
        - 2024

        ---

        :param data_format:
        :type data_format: str

        **Valid values:**
        
        - grib

        
        - netcdf

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_reanalysis_carra_pressure_levels(day: OneOrMore[str], domain: str, leadtime_hour: OneOrMore[str], month: OneOrMore[str], pressure_level: OneOrMore[str], product_type: str, time: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], data_format: str = 'grib'):
    return Collection_reanalysis_carra_pressure_levels.download(day=day, domain=domain, leadtime_hour=leadtime_hour, month=month, pressure_level=pressure_level, product_type=product_type, time=time, variable=variable, year=year, data_format=data_format)
