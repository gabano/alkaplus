'''
Author :    Joao Gabano --  github.com/gabano
Date:       2019-March-09
'''

import csv
import simple_lr

input_file = "alc_example2.csv"
output_file = "resultAlkaplus.txt"



def convertValues(_line):
    '''
     Transforms the values from .csv file into floats, to be used later. Returns a dictionary.
     id, correction_factor, vsample, v1, v2, v3, ph1, ph2, ph3 for each entry on the table
     '''
   
    result = {}
    id_line                         = _line['id']
    correction_factor_line    = float(naRemove(_line['correction_factor']))
    vsample_line                = float(naRemove(_line['vsample']))
    v1_line                         = float(naRemove(_line['v1']))
    v2_line                         = float(naRemove(_line['v2']))   
    v3_line                         = float(naRemove(_line['v3']))
    ph1_line                       = float(naRemove(_line['ph1']))   
    ph2_line                       = float(naRemove(_line['ph2'])) 
    ph3_line                       = float(naRemove(_line['ph3']))

    result = {'id': id_line,
              'correction_factor': correction_factor_line,
              'vsample': vsample_line,
              'v1': v1_line,
              'v2': v2_line,
              'v3': v3_line,
              'ph1': ph1_line,
              'ph2': ph2_line,
              'ph3': ph3_line}
    return result

def naRemove(var):      
    
    if var.upper() == 'NA':
        return 0
    else:
        return var

def buildDataFrame(csvDictFile):
    '''
        Builds a dataframe with the values for each line entry as a dictionary.
        Could've used external lib for that, but I just wanted to code it.
        Maybe not the wisest choice, but it works!
    '''
    i = 0
    tmp_dataframe = {}
    for line in csvDictFile:
        tmp_read = convertValues(line)
        if tmp_read['vsample'] != 0:        # If the vsample is diferent from 0 then write an entry to dataframe. Else pass, ignoring this entry. 
            tmp_dataframe[i] ={i : tmp_read}
        else:
            pass
        i += 1

    return tmp_dataframe

def calculateTotalAlkalinity():
    '''Calculates Total Alkalinity using Gran's method
        based on Carmouze's work 1994 
    '''
    
    tmp_dataframe = {}
    
    for i in dataframe.keys():
     
        vectorVol = [dataframe[i][i]['v1'],dataframe[i][i]['v2'],dataframe[i][i]['v3']]
        vectorF = fCalc(i)
        veq = simple_lr.coefficients(vectorF, vectorVol)[0] #Asks for the interesection/intercept (b0) of original simple linear model
        correction_factor = dataframe[i][i]['correction_factor']
        tmp_Alkalinity =  (veq*(10**(-3))*(0.01*correction_factor*1000)*100000)
        tmp_dataframe[i] = {dataframe[i][i]['id']:  tmp_Alkalinity}

    return tmp_dataframe
  
def fCalc(id_index):
    '''
    Calculates line F, in function of total volume (vsample + titration volume)
    '''
    f_temp = []
    f_temp1 = [dataframe[id_index][id_index]['v1'], dataframe[id_index][id_index]['vsample'], dataframe[id_index][id_index]['ph1']]
    f_temp2 = [dataframe[id_index][id_index]['v2'], dataframe[id_index][id_index]['vsample'], dataframe[id_index][id_index]['ph2']]
    f_temp3 = [dataframe[id_index][id_index]['v3'], dataframe[id_index][id_index]['vsample'], dataframe[id_index][id_index]['ph3']]

    f1= (f_temp1[0]+f_temp1[1])*(10**(-f_temp1[2]))
    f2= (f_temp2[0]+f_temp2[1])*(10**(-f_temp2[2]))
    f3= (f_temp3[0]+f_temp3[1])*(10**(-f_temp3[2]))
    return f1, f2 ,f3
    
def saveOutFile(output_file):

    outAlkaFile = open(output_file, 'w')
    writer = csv.writer(outAlkaFile, quotechar='\"', delimiter = ' ')
    for i in totalAlkalinity.keys():
        writer.writerow([totalAlkalinity[i].keys(), totalAlkalinity[i].values()])

    outAlkaFile.close()

def inspectFile(input_file):

    inAlkaFile = open(input_file, 'r')
    header = []
    result = []
    default_header = ['ID', 'PH1', 'DPH2', 'PH3', 'V1', 'V2', 'V3', 'VSAMPLE', 'CORRECTION_FACTOR']
    header = inAlkaFile.readline()

                
      
    return "Sorry, not implemented yet. Wanna Help?"


#
print("Opening " + input_file +" ...")
inAlkaFile = open(input_file, 'r')
print("Reading csv and parsing to dataframe")
reader = csv.DictReader(inAlkaFile)
dataframe = buildDataFrame(csv.DictReader(inAlkaFile))
inAlkaFile.close()
print("Calculating total alkalinity with parsed parameters")
totalAlkalinity = calculateTotalAlkalinity()
print("Exporting results...")
saveOutFile(output_file)
print("Results exported to " + output_file)
print("Important: Results in uEq of CO2 / liter")




