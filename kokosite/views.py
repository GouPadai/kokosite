from django.shortcuts import render
# from kokoapp.models import kokoform
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
    
    sar   = request.POST.get('sar')
    wot   = request.POST.get('wot')
    obwg   = request.POST.get('obwg')
    wlb   = request.POST.get('wlb')
    csup   = request.POST.get('csup')
    iob   = request.POST.get('iob')
    wys   = request.POST.get('wys')
    wagap   = request.POST.get('wagap')
    hae   = request.POST.get('hae')


    gowwo   = request.POST.get('gowwo')
    twss   = request.POST.get('twss')
    cwei   = request.POST.get('cwei')
    icww   = request.POST.get('icww')
    twnboh   = request.POST.get('twnboh')
    twapf   = request.POST.get('twapf')


    bdnd   = request.POST.get('bdnd')
    iad   = request.POST.get('iad')
    hsfa   = request.POST.get('hsfa')
    ieis   = request.POST.get('ieis')
    wotss   = request.POST.get('wotss')
    raaa   = request.POST.get('raaa')
    aecce   = request.POST.get('aecce')
    oapwtd   = request.POST.get('oapwtd')
    pcf   = request.POST.get('pcf')
    ccmd   = request.POST.get('ccmd')
    maprwu   = request.POST.get('maprwu')
    soits   = request.POST.get('soits')
    gfaet   = request.POST.get('gfaet')
    watdjri   = request.POST.get('watdjri')
    efas   = request.POST.get('efas')
    mcpap   = request.POST.get('mcpap')
    prfaaa   = request.POST.get('prfaaa')
    gotd   = request.POST.get('gotd')
    pcfff   = request.POST.get('pcfff')
    ccda   = request.POST.get('ccda')
    wausaitm   = request.POST.get('wausaitm')
    


    if cn!="default":
        
        
        doc = DocxTemplate("static\\allforms\\templatedonotmove.docx")
        con = { 'cn' : cn , 'en' : en, 'pos' : pos, 'date' : date, 'roleave' : roleave, 'col' : col, 'jwc' : jwc, 'so' : so, 'wwm' : wwm, 'ssc' : ssc, 'cl' : cl, 'seu' : seu, 'at' : at, 'coj' : coj, 
        'sar' : sar,'wot' : wot,'obwg' : obwg,'wlb' : wlb,'csup' : csup,'iob' : iob,'wys' : wys,'wagap' : wagap,
        'hae' : hae,'gowwo' : gowwo,'twss' : twss,'cwei' : cwei,'icww' : icww,'twnboh' : twnboh,'twapf' : twapf,
        'bdnd' : bdnd,'iad' : iad,
        'hsfa' : hsfa,'ieis' : ieis,'wotss' : wotss,'raaa' : raaa,'aecce' : aecce,'oapwtd' : oapwtd,'pcf' : pcf,'ccmd' : ccmd,'maprwu' : maprwu,
        'soits' : soits,'gfaet' : gfaet,'watdjri' : watdjri,'efas' : efas,
        'mcpap' : mcpap,'prfaaa' : prfaaa,'gotd' : gotd,'pcfff' : pcfff,'ccda' : ccda,'wausaitm' : wausaitm,}
        doc.render(con)
        doc.save(f"static\\allforms\\{en}.docx")


        
        
    return render( request, 'index.html' )