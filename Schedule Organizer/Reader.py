import pandas as pd
import Employee
import excelWritter

def getData(filePath):

    data_Cajeros = []
    data_Training = []
    data_SC = []
    data_HC = []
    data_SCH = []
    data_Baggers = []
    data_Cart = []

    # Sheet Names: Cajeros, HC, Cart Boys
    xl_readCajeros = pd.read_excel(filePath, sheet_name='Cajeros')
    xl_readHC = pd.read_excel(filePath, sheet_name='HC')
    xl_readCart = pd.read_excel(filePath, sheet_name='Cart Boys')
    
    flag = False
    for line in xl_readCajeros.values:
        if (line[0] == 'Training'):
            flag = True

        if not flag:
            data_Cajeros.append(tuple(line))
        if flag:
            data_Training.append(tuple(line))
    
    flag = False
    flag2 = False
    for line in xl_readHC.values:
        if (line[0] == 'Head Cashiers'):
            flag = True
        if (line[0] == 'Self Checkout'):
            flag2 = True

        if not flag and not flag2:
            data_SC.append(tuple(line))
        if flag and not flag2:
            data_HC.append(tuple(line))
        if flag2:
            data_SCH.append(tuple(line))
    
    flag = False
    for line in xl_readCart.values:
        if line[0] == 'Cart Boys':
            flag = True

        if not flag:
            data_Baggers.append(tuple(line))
        if flag:
            data_Cart.append(tuple(line))

    # Eliminate Headers
    data_Cajeros = data_Cajeros[3:]
    data_SC = data_SC[3:]
    data_Baggers = data_Baggers[3:]
    data_Training = data_Training[1:]
    data_HC = data_HC[1:]
    data_SCH = data_SCH[1:]
    data_Cart = data_Cart[1:]

    return data_Cajeros, data_Training, data_SC, data_HC, data_SCH, data_Baggers, data_Cart


def getDay(day: str) -> int:
    if day == 'monday':
        dayNum = 1
    elif day == 'tuesday':
        dayNum = 2
    elif day == 'wednesday':
        dayNum = 3
    elif day == 'thursday':
        dayNum = 4
    elif day == 'friday':
        dayNum = 5
    elif day == 'saturday':
        dayNum = 6
    elif day == 'sunday':
        dayNum = 7
    return dayNum


# Needs fix when there are 4 hour shifts that end at 12pm
def day_getShiftsList(day: str, array) -> list:

    result = []

    day_index = getDay(day)
    for i in range(len(array)):

        if (type(array[i][0]) == str and type(array[i][day_index]) == str and array[i][day_index] != 'OFF'):

            emp = Employee.Employee(array[i][0], array[i][day_index])
            result.append(emp)
    
    result.sort(key=lambda x: x.shift_out, reverse=False)

    return result


# Save for Last
# def week_getShiftsLists():
#     return 0


def main(filePath, day):
    
    xlFile = pd.ExcelFile(filePath)

    # ([data_Cajeros], data_Training, data_SC, data_HC, data_SCH, data_Baggers, [data_Cart])
    data = getData(xlFile)

    list_data = list()

    for items in data:
       shifts = day_getShiftsList(day, items)
       list_data.append(shifts)

    excelWritter.write_Plan(list_data)



# main('./BaseHorario.xlsx', 'friday')
    