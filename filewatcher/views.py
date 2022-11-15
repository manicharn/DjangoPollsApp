from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import os
import shutil
import calendar
# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class Movetoerror(View):
    def get(self,request):
        msg={'message':f'success'}
        return JsonResponse(msg)

    def post(self,request):
        data=json.loads(request.body.decode('utf-8'))
        filename=data.get('filename')
        Status=data.get('Status')
        Date=data.get('Date')
    
        srcfile=filename.replace('file:///','')
        filename=filename.replace('file:','')

        filepatharray=filename.split('/')
        print(len(filepatharray))
        # filepatharray[3:7]
        namefile=filepatharray[-1]

        basepath='/'.join(filepatharray[3:7])
        samplepath='/'.join(filepatharray[3:12])
        invtype=filepatharray[10]


        # Date="2022-11-01"
        actualdate=Date.replace("-","")
        Datearry=Date.split("-")
        year=Datearry[0]
        month=Datearry[1]
        monthname=calendar.month_name[int(month)]
        day=Datearry[2]

        if Status=='P':
            basepath=basepath+'/'+'Parked'
            print(basepath)
            if 'dama' in samplepath:
                print('inside dama')
                basepath=basepath+'/'+'dama/ssc/{}/{}/{}/{}'.format(invtype,year,monthname,actualdate)
            elif 'dedm' in samplepath:
                print('inside dedm')
                basepath=basepath+'/'+'dedm/ssc/{}/{}/{}/{}'.format(invtype,year,monthname,actualdate)
            elif 'dmss' in samplepath:
                print('inside dmss')
                basepath=basepath+'/'+'dmss/ssc/{}/{}/{}/{}'.format(invtype,year,monthname,actualdate)
            else:
                print("company code don't match")

        elif Status=='E':
            basepath=basepath+'/'+'Parked'
            basepath
            if 'dama' in samplepath:
                basepath=basepath+'/'+'dama/ssc/ErrorInvoice/{}/{}/{}/{}'.format(invtype,year,monthname,actualdate)
            elif 'dedm' in samplepath:
                basepath=basepath+'/'+'dedm/ssc/ErrorInvoice/{}/{}/{}/{}'.format(invtype,year,monthname,actualdate)
            elif 'dmss' in samplepath:
                basepath=basepath+'/'+'dmss/ssc/ErrorInvoice/{}/{}/{}/{}'.format(invtype,year,monthname,actualdate)
                print(basepath)
            else:
                print("company code don't match")
        else:
            print("status don't match")

        print(basepath)


        if os.path.exists(basepath):
            print('path exist')
        else:
            os.makedirs(basepath)
            print('directory created')

        dstfile=os.path.join(basepath,namefile)
        dstfile=dstfile.replace("\\","/")
        shutil.move(srcfile,dstfile)




        result={'result':dstfile}
        return JsonResponse(result)
