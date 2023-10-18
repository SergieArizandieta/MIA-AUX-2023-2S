from Analyzer.Analyzer import Commands

def readData(data):
   data = data.replace('\r', '')
   array = data.split('\n')
   array = [elemento for elemento in array if elemento != '']
   return Commands(array)
