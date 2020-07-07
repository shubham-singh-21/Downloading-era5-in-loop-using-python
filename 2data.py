
import cdsapi
import calendar

c = cdsapi.Client()

def retrieve_era5():
    #list=[]
    yearStart = 2014
    yearEnd = 2014
    monthStart = 1
    monthEnd = 1
    days=[
            '01','02','03',
            '04','05','06',
            '07','08','09',
            '10','11','12',
            '13','14','15',
            '16','17','18',
            '19','20','21',
            '22','23','24',
            '25','26','27',
            '28','29','30',
            '31'
        ]
    for year in list(range(yearStart, yearEnd + 1)):
        for month in list(range(monthStart, monthEnd + 1)):
            yr =  str(year) 
            mn = str(month).zfill(2)
            dy = days
            
#            startDate = '%04d%02d%02d' % (year, month, 1)
#            numberOfDays = calendar.monthrange(year, month)[1]
#            lastDate = '%04d%02d%02d' % (year, month, numberOfDays)

            target = "era5_daily_%04d%02d.nc" % (year, month)

#            requestDates = (startDate + "/TO/" + lastDate)
#            print yr,mn,dy
            era5_request(yr,mn,dy, target)

def era5_request(y,m,d, target): 

  c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type':'reanalysis',
        'variable':[
            'geopotential','potential_vorticity','relative_humidity',
            'specific_humidity','temperature','u_component_of_wind',
            'v_component_of_wind','vertical_velocity','vorticity'
        ],
        'pressure_level':[
            '1','2','3',
            '5','7','10',
            '20','30','50',
            '70','100','125',
            '150','175','200',
            '225','250','300',
            '350','400','450',
            '500','550','600',
            '650','700','750',
            '775','800','825',
            '850','875','900',
            '925','950','975',
            '1000'
            ],
        'year':y,
        'month':m,
        'day': d,
        'time':[
            '00:00','06:00','12:00',
            '18:00'
        ],
        'grid':['.5','.5'],
        'format':'netcdf',
        
    }, target)
if __name__ == '__main__':
    retrieve_era5()
