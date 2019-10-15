import csv
import dateutil.parser
from os import listdir
from os.path import isfile, join
import argparse
import datetime

# open file, create a reader from csv.DictReader, and read input times and values
class ImportData:
    def __init__(self, data_csv):
        self._time = []
        self._value = []
        self._roundtime = []
        self.roundtimeStr = []
        self._duplicateTime = []
        self._indices = []
        self._avg = []
        self._final_rounded = []
        with open(data_csv, "r") as fhandle:
            reader = csv.DictReader(fhandle)
            for row in reader:
                try:
                    self._time.append(dateutil.parser.parse(row['time']))
                except ValueError:
                    print('Bad input format for time')
                    print(row['time'])
                self._value.append(row['value'])
            fhandle.close()

    def roundTimeArray(self, resolution):
        for times in self._time:
                minminus = datetime.timedelta(minutes = (times.minute % resolution))
                minplus = datetime.timedelta(minutes=resolution) - minminus
                if (times.minute % resolution) <= resolution/2:
                    newtime = times - minminus
                else:
                    newtime=times + minplus
                self._roundtime.append(newtime)
                #self._roundtimeStr.append(newtime.strftime("%m/%d/%Y %H:%M"))
        #print(self._roundtime)
        return(self._roundtime)
        
    # return list of value(s) associated with key_time
    # if none, return -1 and error message
    def linear_search_value(self, key_time):
        for i in range(len(self._roundtime)):
            curr = self._roundtime[i]
            if key_time == curr:
                self._duplicateTime.append(self._roundtime[i])
                self._indices.append(i)
        TimeLen = len(self._duplicateTime)
        if TimeLen > 1:
            self._avg = [float(self._value[x]) for x in self._indices]
            avg_sum = sum(self._avg)
            self._avg = str(avg_sum)
            duplicate_index = self._duplicateTime[1]
            print(duplicate_index)
            print(avg_sum)
            for num in self._roundtime: 
                if num not in self._final_rounded: 
                    self._final_rounded.append(num) 
            self._value.pop((self._indices[1]))
            replace_index = (self._final_rounded.index(duplicate_index))
            

        #         curr = self._value[i]
        #         if self._indices == curr:
                # tempFloat = self._indices
                # print(tempFloat)
                # summedValues = TimeLen*tempFloat
                # Float2Str = str(summedValues)
                # print(Float2Str)
               # return -1

    # def linear_search_time(self, value):
    #     for i in range(len(self._indices)):
    #         curr = self._indices[i]
    #         if self._value[i] == curr:
    #             self._duplicateTime.append(self._time[i])
    #     TimeLen = len(self._duplicateTime)
    #     if TimeLen > 1:
    #         tempFloat = float(value)
    #         summedValues = TimeLen*tempFloat
    #         Float2Str = str(summedValues)
    #     return -1

    # optional extra credit
    # return list of value(s) associated with key_time
    # # if none, return -1 and error message
    # def binary_search_value(self,key_time):
    # lo = -1
    # hi = len(self.roundtimeStr):
    # while (hi - lo > 1):
    #     mid = (hi + lo) // 2
    #     if key_time ==  self.roundtimeStr[mid]:
    #         return self._value[mid]
    #     elif ( key_time < self.roundtimeStr[mid] ):
    #         hi = mid  
    #         return self._value[mid]   
    #     else:
    #         lo = mid
    #         return self._value[mid]
    # return -1

    # Inputs: obj (ImportData Object) and res (rounding resoultion)
    # objective:
    # create a list of datetime entries and associated values
    # with the times rounded to the nearest rounding resolution (res)
    # ensure no duplicated times
    # handle duplicated values for a single timestamp based on instructions in
    # the assignment
    # return: iterable zip object of the two lists
    # note: you can create additional variables to help with this task
    # which are not returned


#def printArray(data_list, annotation_list, base_name, key_file):
    # combine and print on the key_file

if __name__ == '__main__':

    # #adding arguments
    # parser = argparse.ArgumentParser(description= 'A class to import, combine, and print data from a folder.',
    # prog= 'dataImport')

    # parser.add_argument('folder_name', type = str, help = 'Name of the folder')

    # parser.add_argument('output_file', type=str, help = 'Name of Output file')

    # parser.add_argument('sort_key', type = str, help = 'File to sort on')

    # parser.add_argument('--number_of_files', type = int,
    # help = "Number of Files", required = False)

    # args = parser.parse_args()

    time = datetime.datetime(2018, 3, 17, 9, 45)
    value = '0.7'
    resolution = 15
    data_csv = 'bolus_small.csv'
    ID = ImportData(data_csv)
    ID.roundTimeArray(resolution)
    ID.linear_search_value(time)
    #ID.linear_search_time(value)

    #pull all the folders in the file
    #files_lst = # list the folders


    #import all the files into a list of ImportData objects (in a loop!)
    #data_lst = []

    #create two new lists of zip objects
    # do this in a loop, where you loop through the data_lst
    #data_5 = [] # a list with time rounded to 5min
    #data_15 = [] # a list with time rounded to 15min

    #print to a csv file
    #printLargeArray(data_5,files_lst,args.output_file+'_5',args.sort_key)
    #printLargeArray(data_15, files_lst,args.output_file+'_15',args.sort_key)
