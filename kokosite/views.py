from django.shortcuts import render
from kokoapp.models import kokoform
from docxtpl import DocxTemplate


def index(request):
    cn = request.POST.get('cn','default')
    en = request.POST.get('en')
    pos = request.POST.get('pos')
    date = request.POST.get('date')
    roleave1 = request.POST.getlist('checkboxes')
    roleave=''
    if(len(roleave1)>0):
        for data1 in roleave1:
            roleave=roleave+data1 +" , " 
    
    col = request.POST.get('col')

    jwc = request.POST.get('jwc')
    so  = request.POST.get('so')
    wwm  = request.POST.get('wwm')
    ssc  = request.POST.get('ssc')
    cl  = request.POST.get('cl')
    seu  = request.POST.get('seu')
    at  = request.POST.get('at')
    coj   = request.POST.get('coj')


    if cn!="default":
        
        
        doc = DocxTemplate("static\\allforms\\templatedonotmove.docx")
        con = { 'cn' : cn , 'en' : en, 'pos' : pos, 'date' : date, 'roleave' : roleave, 'col' : col, 'jwc' : jwc, 'so' : so, 'wwm' : wwm, 'ssc' : ssc, 'cl' : cl, 'seu' : seu, 'at' : at, 'coj' : coj}
        doc.render(con)
        doc.save(f"kokosite\\allforms\\{en}.docx")


        
        forms= kokoform( Company_name=cn, Employee_name=en, Posistion=pos, Date=date, ReasonOfLeave=roleave, CommentOnLeave =col, JobWasChallenging=jwc, SufficientOpportunities = so,ManageableWorkload = wwm, SufficientResources=ssc, OthersBehaviour = cl,SkillsEffectivelyUsed =seu,AdequateTrainingPrograms=at,ImprovementInJobPossible=coj) 
        forms.save()
        context = {
            'filename': f"static\\allforms\\{en}_{pos}_{date}.docx",
        }
    return render( request, 'index.html' )