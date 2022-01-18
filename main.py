from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
import time
import os
from datetime import date
import re
from zipfile import ZipFile
from os import listdir
import shutil
from pathlib import Path

ws = Tk()
ws.title('Промяна HTML атрибути')
windowWidth = ws.winfo_reqwidth()
windowHeight = ws.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(ws.winfo_screenwidth() / 5 - windowWidth / 2)
positionDown = int(ws.winfo_screenheight() / 7 - windowHeight / 2)
ws.geometry("+{}+{}".format(positionRight, positionDown))





# НАЧАЛО НА СТЪПКА 1

def open_file_zip(zipbutton):
    zipbutton["state"] = "disabled"
    warn = Label(
        ws,
        text='Моля, изчакайте !',
        foreground='red'
    )
    warn.grid(row=1, column=0, padx=10, pady=20)
    zip_path = askopenfilename()
    zip_name = (os.path.basename(zip_path))
    #print(zip_path)
    zip_name_noext = os.path.splitext(zip_name)[0]
    zip_path_noext = os.path.splitext(zip_path)[0]
    #print(zip_path_noext)

    with ZipFile(zip_path, 'r') as zipObj:
        listOfiles = zipObj.namelist()
        #print(listOfiles)
        p = Path(listOfiles[0])
        if str(p.parent) == '.':
            p = Path(listOfiles[1])
        #print(p.parent)
        zip_main_folder = str(p.parent)
        ppp = Path(zip_path)
        main_path = '/'.join(ppp.parts[0:-1])
        zipObj.extractall(path=main_path)

    working_dir = (os.path.dirname(zip_path_noext)+'/'+zip_main_folder) #Името на мейн фолдъре, както се разархивира
    #print(working_dir)
    main_dir_folders = [f for f in listdir(working_dir)] #Имената на всички фолдър във основната
    #print('main_dir: '+ ' '.join(main_dir_folders))
    xhtml_name = [f for f in listdir(working_dir+'/reports')]


    fold_list = ['META-INF', 'reports']
    company_name = list(set(main_dir_folders)-set(fold_list)) #Името на 3тия фолдър
    new_fold_str = '/xbrl/2020'
    old_fold_str = '/xbrl/2019'




    if ch1.get() == 1 and ch0.get() == 0:
        try:
            os.rename(working_dir + '/' + ' '.join(company_name) + old_fold_str, working_dir + '/' +
                      ' '.join(company_name) + new_fold_str)
            xmls_names = [f for f in listdir(working_dir + '/' + ' '.join(company_name) + new_fold_str)]

            all_files_paths = [working_dir + '/META-INF/catalog.xml', working_dir + '/META-INF/taxonomyPackage.xml',
                               working_dir + '/reports/' + ' '.join(xhtml_name)]

            for xmls in xmls_names:
                all_files_paths.append(working_dir + '/' + ' '.join(company_name) + new_fold_str + '/' + xmls)


        except FileNotFoundError:
            raise
    else:
        xmls_names = [f for f in listdir(working_dir + '/' + ' '.join(company_name) + old_fold_str)]



        all_files_paths = [working_dir + '/META-INF/catalog.xml', working_dir + '/META-INF/taxonomyPackage.xml',
                           working_dir + '/reports/' + ' '.join(xhtml_name)]

        for xmls in xmls_names:
            all_files_paths.append(working_dir + '/'+ ' '.join(company_name) + old_fold_str +'/'+xmls)

    '''if ch2.get() == 1:
        et = xml.etree.ElementTree.parse(working_dir+'/'+'META-INF'+'/'+'taxonomyPackage.xml')
        root = et.getroot()

        for tags in root.iter('*'):
            if tags.text is not None:
                tags.text = tags.text.replace("Taxonomy 2019", "Taxonomy 2020")

        et.write(working_dir+'/'+'META-INF'+'/'+'taxonomyPackage.xml')'''

    for files in all_files_paths:
        p = Path(files)
        try:
            #print(files)
            if ch0.get() == 0:
                with open(files, "r+", encoding="utf-8") as f:
                    fold_link = '/xbrl/2019'
                    fold_link_new = '/xbrl/2020'
                    str_old_0 = 'Taxonomy 2019'
                    str_new_0 = 'Taxonomy 2020'
                    str_old_1 = 'xmlns:ifrs-full="http://xbrl.ifrs.org/taxonomy/2019-03-27/ifrs-full"'
                    str_new_1 = 'xmlns:ifrs-full="http://xbrl.ifrs.org/taxonomy/2020-03-16/ifrs-full"'
                    str_old_2 = '/xbrl.ifrs.org/taxonomy/2019-03-27/full_ifrs/full_ifrs-cor_2019-03-27.xsd'
                    str_new_2 = '/xbrl.ifrs.org/taxonomy/2020-03-16/full_ifrs/full_ifrs-cor_2020-03-16.xsd'
                    str_old_3 = '2019-03-27'
                    str_new_3 = '2020-03-16'
                    str_old_4 = '/www.eurofiling.info/xbrl/esef/role/all/ias_1_role-110000'
                    str_new_4 = '/www.esma.europa.eu/xbrl/role/all/ias_1_role-110000'
                    str_old_5 = '/www.eurofiling.info/xbrl/esef/role/all/ias_1_role-210000'
                    str_new_5 = '/www.esma.europa.eu/xbrl/role/all/ias_1_role-210000'
                    str_old_6 = '/www.eurofiling.info/xbrl/esef/role/all/ias_1_role-320000'
                    str_new_6 = '/www.esma.europa.eu/xbrl/role/all/ias_1_role-320000'
                    str_old_7 = '/www.eurofiling.info/xbrl/esef/role/all/ias_1_role-420000'
                    str_new_7 = '/www.esma.europa.eu/xbrl/role/all/ias_1_role-420000'
                    str_old_8 = '/www.eurofiling.info/xbrl/esef/role/all/ias_7_role-510000'
                    str_new_8 = '/www.esma.europa.eu/xbrl/role/all/ias_7_role-510000'
                    str_old_9 = '/www.eurofiling.info/xbrl/esef/role/all/ias_1_role-610000'
                    str_new_9 = '/www.esma.europa.eu/xbrl/role/all/ias_1_role-610000'
                    str_old_10 = ' preferredLabel="http://www.xbrl.org/2003/role/totalLabel"'
                    str_new_10 = ''
                    str_old_11 = ' preferredLabel="http://www.xbrl.org/2009/role/negatedLabel"'
                    str_new_11 = ''
                    str_old_12 = ' preferredLabel="http://www.xbrl.org/2009/role/negatedTerseLabel"'
                    str_new_12 = ''
                    str_old_13 = ' preferredLabel="http://www.xbrl.org/2003/role/terseLabel"'
                    str_new_13 = ''
                    str_old_14 = ' preferredLabel="http://www.xbrl.org/2003/role/periodStartLabel"'
                    str_new_14 = ''
                    str_old_15 = ' preferredLabel="http://www.xbrl.org/2003/role/periodEndLabel"'
                    str_new_15 = ''
                    str_old_16 = ' preferredLabel="http://www.xbrl.org/2009/role/negatedTotalLabel"'
                    str_new_16 = ''
                    str_old_17 = ' preferredLabel="http://www.xbrl.org/2009/role/netLabel"'
                    str_new_17 = ''
                    str_old_18 = 'ReserveForCatastropheMember'
                    str_new_18 = 'StatutoryReserveMember'
                    newline = []
                    for line in f.readlines():

                        if str_old_0 in line and ch2.get() == 1:
                            newline.append(line.replace(str_old_0, str_new_0))
                        elif str_old_1 in line and ch3.get() == 1:
                            newline.append(line.replace(str_old_1, str_new_1))
                        elif str_old_2 in line and ch4.get() == 1:
                            r1 = line.replace(str_old_2, str_new_2)
                            r2 = r1.replace(str_old_18, str_new_18)
                            newline.append(r2)
                        elif str_old_3 in line and ch5.get() == 1:
                            e1 = line.replace(str_old_3, str_new_3)
                            e2 = e1.replace(fold_link, fold_link_new)
                            if ch1.get() == 1:
                                newline.append(e2)
                            else:
                                newline.append(e1)
                        elif str_old_4 in line and ch6.get() == 1:
                            newline.append(line.replace(str_old_4, str_new_4))
                        elif str_old_5 in line and ch7.get() == 1:
                            newline.append(line.replace(str_old_5, str_new_5))
                        elif str_old_6 in line and ch8.get() == 1:
                            newline.append(line.replace(str_old_6, str_new_6))
                        elif str_old_7 in line and ch9.get() == 1:
                            newline.append(line.replace(str_old_7, str_new_7))
                        elif str_old_8 in line and ch10.get() == 1:
                            newline.append(line.replace(str_old_8, str_new_8))
                        elif str_old_9 in line and ch11.get() == 1:
                            newline.append(line.replace(str_old_9, str_new_9))
                        elif str_old_10 in line and ch12.get() == 1:
                            newline.append(line.replace(str_old_10, str_new_10))
                        elif str_old_11 in line and ch13.get() == 1:
                            newline.append(line.replace(str_old_11, str_new_11))
                        elif str_old_12 in line and ch14.get() == 1:
                            newline.append(line.replace(str_old_12, str_new_12))
                        elif str_old_13 in line and ch15.get() == 1:
                            newline.append(line.replace(str_old_13, str_new_13))
                        elif str_old_14 in line and ch16.get() == 1:
                            newline.append(line.replace(str_old_14, str_new_14))
                        elif str_old_15 in line and ch17.get() == 1:
                            newline.append(line.replace(str_old_15, str_new_15))
                        elif str_old_16 in line and ch18.get() == 1:
                            newline.append(line.replace(str_old_16, str_new_16))
                        elif str_old_17 in line and ch19.get() == 1:
                            newline.append(line.replace(str_old_17, str_new_17))
                        elif str_old_18 in line:
                            newline.append(line.replace(str_old_18, str_new_18))

                        elif ch1.get() == 1:
                            newline.append(line.replace(fold_link, fold_link_new))

                        else:
                            newline.append(line)

                p = Path(files)
                new_name = os.path.join(str(p.parent),
                                        str(p.parent) + '/' + os.path.splitext(p.name)[0] + "_NEW" + p.suffix)
                with open(new_name, "w", encoding="utf-8") as f:
                    for line in newline:
                        f.writelines(line)
                os.remove(files)

                os.rename(str(p.parent) + '/' + os.path.splitext(p.name)[0] + "_NEW" + p.suffix,
                          str(p.parent) + '/' + os.path.splitext(p.name)[0] + p.suffix)
            else:
                if '_cal.xml' in files:
                    with open(files, "r+", encoding="utf-8") as f:
                        nline = []
                        for line1 in f.readlines():
                            if '"NoncurrentLiabilities" xlink:to="CurrentTaxLiabilitiesNoncurrent" order="4.0" weight="1"/>' in line1:
                                nline.append(line1)
                                nline.append(
                                    '    <link:loc xlink:type="locator" xlink:href="http://xbrl.ifrs.org/taxonomy/2019-03-27/full_ifrs/full_ifrs-cor_2019-03-27.xsd#ifrs-full_NoncurrentLeaseLiabilities" xlink:label="NoncurrentLeaseLiabilities"/>\n')
                                nline.append('    <link:calculationArc xlink:type="arc" xlink:arcrole="http://www.xbrl.org/2003/arcrole/summation-item" xlink:from="NoncurrentLiabilities" xlink:to="NoncurrentLeaseLiabilities" order="4.1" weight="1"/>\n')
                            elif '"CurrentLiabilitiesOtherThanLiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale" xlink:to="CurrentTaxLiabilitiesCurrent" order="3.0" weight="1"/>' in line1:
                                nline.append(line1)
                                nline.append('    <link:loc xlink:type="locator" xlink:href="http://xbrl.ifrs.org/taxonomy/2019-03-27/full_ifrs/full_ifrs-cor_2019-03-27.xsd#ifrs-full_CurrentLeaseLiabilities" xlink:label="CurrentLeaseLiabilities"/>\n')
                                nline.append('    <link:calculationArc xlink:type="arc" xlink:arcrole="http://www.xbrl.org/2003/arcrole/summation-item" xlink:from="CurrentLiabilitiesOtherThanLiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale" xlink:to="CurrentLeaseLiabilities" order="3.1" weight="1"/>\n')
                            elif 'xlink:from="loc_4" xlink:to="loc_16" order="30.0" weight="-1"/>' in line1:
                                nline.append(line1)
                                nline.append('    <link:loc xlink:type="locator" xlink:href="http://xbrl.ifrs.org/taxonomy/2019-03-27/full_ifrs/full_ifrs-cor_2019-03-27.xsd#ifrs-full_CostOfMerchandiseSold" xlink:label="loc_60"/>\n')
                                nline.append('    <link:calculationArc xlink:type="arc" xlink:arcrole="http://www.xbrl.org/2003/arcrole/summation-item" xlink:from="loc_4" xlink:to="loc_60" order="30.1" weight="-1"/>\n')
                            elif 'xlink:from="loc_4" xlink:to="loc_20" order="50.0" weight="-1"/>' in line1:
                                nline.append(line1)
                                nline.append('    <link:loc xlink:type="locator" xlink:href="http://xbrl.ifrs.org/taxonomy/2019-03-27/full_ifrs/full_ifrs-cor_2019-03-27.xsd#ifrs-full_ServicesExpense" xlink:label="loc_89"/>\n')
                                nline.append('    <link:calculationArc xlink:type="arc" xlink:arcrole="http://www.xbrl.org/2003/arcrole/summation-item" xlink:from="loc_4" xlink:to="loc_89" order="50.1" weight="-1"/>\n')

                            else:
                                nline.append(line1)

                    p = Path(files)
                    new_name = os.path.join(str(p.parent),
                                            str(p.parent) + '/' + os.path.splitext(p.name)[0] + "_NEW" + p.suffix)
                    with open(new_name, "w", encoding="utf-8") as f:
                        for line1 in nline:
                            f.writelines(line1)
                    if '_cal.xml' in files:
                        os.remove(files)

                        os.rename(str(p.parent) + '/' + os.path.splitext(p.name)[0] + "_NEW" + p.suffix,
                                  str(p.parent) + '/' + os.path.splitext(p.name)[0] + p.suffix)





        except:

            raise



    #shutil.make_archive(zip_name_noext+'_New', 'zip', zip_name_noext)
    #shutil.rmtree(zip_path_noext)
    time.sleep(1.5)
    warn.destroy()
    zipbutton["state"] = "enable"

# КРАЙ НА СТЪПКА 1




# НАЧАЛО НА СТЪПКА 2


def open_file_xhtml(adharbtn):
    adharbtn["state"]="disabled"
    warn = Label(
        ws,
        text='Моля, изчакайте !',
        foreground='red'
    )

    warn.grid(row=1, column=0, padx=10, pady=20)
    file_path = askopenfilename()

    try:
        with open (file_path, "r+", encoding="utf-8") as f:
            newline = []
            corp_name_all = ''
            for line in f.readlines():

                if 'Current Year' in line:
                    newline.append(line.replace('Current Year', 'Текуща година'))
                elif 'easyESEF' in line:
                    today = str(date.today())
                    newline.append('<!-- Изготвено за Вас на '+today+'-->')


                elif 'name="ifrs-full:NameOfReportingEntityOrOtherMeansOfIdentification"' in line:
                    result = re.search('">(.*)</', line)
                    #global corp_name
                    corp_name = re.search('>(.*)<', str(result.group(1)))
                    corp_name_all = corp_name.group(1)
                    newline.append(line)
                elif '>INDEX<' in line:

                    newline.append(line.replace('>INDEX<', '>'+corp_name_all+'<'))

                elif 'LEI (Legal Entity Identifier) of reporting entity' in line:
                    newline.append(line.replace('LEI (Legal Entity Identifier) of reporting entity',
                                                'КОД: LEI (Legal Entity Identifier) на дружеството'))

                elif 'URL (Uniform Resource Locator) of entity web site' in line:
                    newline.append(line.replace('URL (Uniform Resource Locator) of entity web site',
                                                'URL (Uniform Resource Locator)'))

                elif 'Notes' in line:
                    newline.append(line.replace('Notes',
                                                'Бел.'))
                elif 'Annual Report ESEF' in line:
                    newline.append(line.replace('Annual Report ESEF',
                                                'Консолидиран финансов отчет'))
                elif 'sign="-"name' in line:
                    newline.append(line.replace('sign="-"name',
                                                'sign="-" name'))
                elif 'Previous Year' in line:
                    newline.append(line.replace('Previous Year', 'Предходна година'))
                elif '[000000] Reporting entity' in line:
                    newline.append(line.replace('[000000] Reporting entity', 'Обща информация за дружеството'))
                elif '[000000]' in line:
                    newline.append(line.replace('[000000]', ''))
                elif '[110000]' in line:
                    newline.append(line.replace('[110000]', ''))
                elif '[210000]' in line:
                    newline.append(line.replace('[210000]', ''))
                elif '[220000]' in line:
                    newline.append(line.replace('[220000]', ''))
                elif '[310000]' in line:
                    newline.append(line.replace('[310000]', ''))
                elif '[320000]' in line:
                    newline.append(line.replace('[320000]', ''))
                elif '[410000]' in line:
                    newline.append(line.replace('[410000]', ''))
                elif '[420000]' in line:
                    newline.append(line.replace('[420000]', ''))
                elif '[510000]' in line:
                    newline.append(line.replace('[510000]', ''))
                elif '[520000]' in line:
                    newline.append(line.replace('[520000]', ''))
                elif '[610000]' in line:
                    newline.append(line.replace('[610000]', ''))

                elif '[Total]' in line:
                    newline.append(line.replace('[Total]', 'ОБЩО'))
                elif '[TOTAL]' in line:
                    newline.append(line.replace('[TOTAL]', 'ОБЩО'))

                elif 'Beginning' in line:
                    newline.append(line.replace('Beginning', 'Начало'))
                elif '>End<' in line:
                    newline.append(line.replace('>End<', '>Край<'))
                elif 'Description' in line:
                    newline.append(line.replace('>Description<', '>Описание<'))

                elif '[AT END OF PERIOD]' in line:
                    newline.append(line.replace('[AT END OF PERIOD]', '[В края на периода]'))

                elif '[AT BEGINNING OF PERIOD]' in line:
                    newline.append(line.replace('[AT BEGINNING OF PERIOD]', '[В началото на периода]'))

                elif 'Увеличение (намаление) на материалните запаси от готова продукция и незавършено производство' in line:
                    newline.append(line.replace('Увеличение (намаление) на материалните запаси от готова продукция и незавършено производство',
                                                'Намаление(Увеличение) на материалните запаси от готова продукция и незавършено производство'))
                elif '„Използвани суровини, материали и консумативи“;' in line:
                    newline.append(line.replace(
                        '„Използвани суровини, материали и консумативи“;',
                        'Използвани суровини, материали и консумативи'))
                elif 'Приходи (разходи) за (от) данъци' in line:
                    newline.append(line.replace(
                        'Приходи (разходи) за (от) данъци',
                        'Разходи (приходи) за (от) данъци'))
                elif 'id="_510000_B32" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Възстановени (платени) данъци върху дохода' in line:
                    newline.append(line.replace(
                        'id="_510000_B32" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Възстановени (платени) данъци върху дохода',
                        'id="_510000_B32" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Платени (възстановени) данъци върху дохода, класифицирани като оперативни дейности'))
                elif 'id="_510000_B28" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Изплатени дивиденти' in line:
                    newline.append(line.replace(
                        'id="_510000_B28" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Изплатени дивиденти',
                        'id="_510000_B28" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Изплатени дивиденти, класифицирани като оперативни дейности'))
                elif 'id="_510000_B29" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Получени дивиденти' in line:
                    newline.append(line.replace(
                        'id="_510000_B29" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Получени дивиденти',
                        'id="_510000_B29" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Получени дивиденти, класифицирани като оперативни дейности'))
                elif 'id="_510000_B30" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Платени лихви' in line:
                    newline.append(line.replace(
                        'id="_510000_B30" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Платени лихви',
                        'id="_510000_B30" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Платени лихви, класифицирани като оперативни дейности'))
                elif 'id="_510000_B31" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Получени лихви' in line:
                    newline.append(line.replace(
                        'id="_510000_B31" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Получени лихви',
                        'id="_510000_B31" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Получени лихви, класифицирани като оперативни дейности'))
                elif 'id="_510000_B33" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Други входящи (изходящи) парични средства' in line:
                    newline.append(line.replace(
                        'id="_510000_B33" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Други входящи (изходящи) парични средства',
                        'id="_510000_B33" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:29.04px;width:61.735%;">Други входящи (изходящи) парични средства, класифицирани като оперативни дейности'))
                elif 'id="_510000_B37" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Парични потоци' in line:
                    newline.append(line.replace(
                        'id="_510000_B37" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Парични потоци',
                        'id="_510000_B37" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Парични потоци, използвани за получаване на контрол върху дъщерни предприятия или други стопански субекти, класифицирани като инвестиционни дейности'))
                elif 'Постъпления от продажби на имоти' in line:
                    newline.append(line.replace(
                        'Постъпления от продажби на имоти',
                        'Постъпления от продажби на имоти, машини и съоръжения, класифицирани като инвестиционни дейности'))
                elif 'Закупуване на имоти' in line:
                    newline.append(line.replace(
                        'Закупуване на имоти',
                        'Закупуване на имоти, машини и съоръжения, класифицирани като инвестиционни дейности'))
                elif 'Постъпления от продажби на нематериални активи' in line:
                    newline.append(line.replace(
                        'Постъпления от продажби на нематериални активи',
                        'Постъпления от продажби на нематериални активи, класифицирани като инвестиционни дейности'))
                elif 'Закупуване на нематериални активи' in line:
                    newline.append(line.replace(
                        'Закупуване на нематериални активи',
                        'Закупуване на нематериални активи, класифицирани като инвестиционни дейности'))
                elif 'Постъпления от продажби на дълготрайни активи' in line:
                    newline.append(line.replace(
                        'Постъпления от продажби на дълготрайни активи',
                        'Постъпления от продажби на дълготрайни активи, класифицирани като инвестиционни дейности'))
                elif 'Закупуване на други дълготрайни активи' in line:
                    newline.append(line.replace(
                        'Закупуване на други дълготрайни активи',
                        'Закупуване на други дълготрайни активи, класифицирани като инвестиционни дейности'))
                elif 'id="_510000_B48" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Постъпления от предоставени от държавата безвъзмездни средства' in line:
                    newline.append(line.replace(
                        'id="_510000_B48" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Постъпления от предоставени от държавата безвъзмездни средства',
                        'id="_510000_B48" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Постъпления от предоставени от държавата безвъзмездни средства, класифицирани като инвестиционни дейности'))
                elif 'Парични авансови плащания и заеми' in line:
                    newline.append(line.replace(
                        'Парични авансови плащания и заеми',
                        'Парични авансови плащания и заеми, предоставени на други лица, класифицирани като инвестиционни дейности'))
                elif 'Парични постъпления от погасяването на авансови плащания и заеми' in line:
                    newline.append(line.replace(
                        'Парични постъпления от погасяването на авансови плащания и заеми',
                        'Парични постъпления от погасяването на авансови плащания и заеми, предоставени на други лица, класифицирани като инвестиционни дейности'))
                elif 'Парични плащания за фючърсни договори' in line:
                    newline.append(line.replace(
                        'Парични плащания за фючърсни договори',
                        'Парични плащания за фючърсни договори, форуърдни договори, опционни договори и суапови договори, класифицирани като инвестиционни дейности'))
                elif 'Парични постъпления от фючърсни договори' in line:
                    newline.append(line.replace(
                        'Парични постъпления от фючърсни договори',
                        'Парични постъпления от фючърсни договори, форуърдни договори, опционни договори и суапови договори, класифицирани като инвестиционни дейности'))
                elif 'id="_510000_B53" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Получени дивиденти' in line:
                    newline.append(line.replace(
                        'id="_510000_B53" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Получени дивиденти',
                        'id="_510000_B53" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Получени дивиденти, класифицирани като инвестиционни дейности'))
                elif 'id="_510000_B54" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Платени лихви' in line:
                    newline.append(line.replace(
                        'id="_510000_B54" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Платени лихви',
                        'id="_510000_B54" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Платени лихви, класифицирани като инвестиционни дейности'))
                elif 'id="_510000_B55" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Получени лихви' in line:
                    newline.append(line.replace(
                        'id="_510000_B55" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Получени лихви',
                        'id="_510000_B55" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Получени лихви, класифицирани като инвестиционни дейности'))
                elif 'id="_510000_B56" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Възстановени (платени) данъци върху дохода' in line:
                    newline.append(line.replace(
                        'id="_510000_B56" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Възстановени (платени) данъци върху дохода',
                        'id="_510000_B56" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Платени (възстановени) данъци върху дохода, класифицирани като инвестиционни дейности'))
                elif 'Постъпления от получени заеми' in line:
                    newline.append(line.replace(
                        'Постъпления от получени заеми',
                        'Постъпления от получени заеми, класифицирани като финансови дейности'))
                elif 'Погасяване на получени заеми' in line:
                    newline.append(line.replace(
                        'Погасяване на получени заеми',
                        'Погасяване на получени заеми, класифицирани като финансови дейности'))
                elif 'id="_510000_B69" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Постъпления от предоставени от държавата безвъзмездни средства' in line:
                    newline.append(line.replace(
                        'id="_510000_B69" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Постъпления от предоставени от държавата безвъзмездни средства',
                        'id="_510000_B69" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Постъпления от предоставени от държавата безвъзмездни средства, класифицирани като финансови дейности'))
                elif 'id="_510000_B70" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Изплатени дивиденти' in line:
                    newline.append(line.replace(
                        'id="_510000_B70" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Изплатени дивиденти',
                        'id="_510000_B70" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Изплатени дивиденти, класифицирани като финансови дейности'))
                elif 'id="_510000_B71" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Платени лихви' in line:
                    newline.append(line.replace(
                        'id="_510000_B71" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Платени лихви',
                        'id="_510000_B71" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Платени лихви, класифицирани като финансови дейности'))
                elif 'id="_510000_B72" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Възстановени (платени) данъци върху дохода' in line:
                    newline.append(line.replace(
                        'id="_510000_B72" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Възстановени (платени) данъци върху дохода',
                        'id="_510000_B72" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Платени (възстановени) данъци върху дохода, класифицирани като финансови дейности'))
                elif 'id="_510000_B73" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Други входящи (изходящи) парични средства' in line:
                    newline.append(line.replace(
                        'id="_510000_B73" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Други входящи (изходящи) парични средства',
                        'id="_510000_B73" style="border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;text-align:left;padding-left:19.36px;width:61.735%;">Други входящи (изходящи) парични средства, класифицирани като финансови дейности'))
                elif 'Резерв за катастрофични събития' in line:
                    newline.append(line.replace(
                        'Резерв за катастрофични събития',
                        'Законов резерв'))
                elif '>Други разходи<' in line:
                    newline.append(line.replace(
                        '>Други разходи<',
                        '>Други разходи, по икономически елементи<'))
                elif '[Net]' in line:
                    newline.append(line.replace(
                        '[Net]',
                        'НЕТО '))





                else:
                    newline.append(line)

        save_path_1 = os.path.dirname(os.path.abspath(file_path))

        p = Path(file_path)
        completeName_1 = os.path.join(save_path_1, str(p.parent) + '/' + os.path.splitext(p.name)[0] + "_NEW" + p.suffix)

        with open(completeName_1, "w", encoding="utf-8") as f:
            for line in newline:
                f.writelines(line)

        os.remove(file_path)
        os.rename(str(p.parent) + '/' + os.path.splitext(p.name)[0] + "_NEW" + p.suffix,
                  str(p.parent) + '/' + os.path.splitext(p.name)[0] + p.suffix)

        ######################
        with open(file_path, "r+", encoding="utf-8") as f:
            new_line = []
            colors_reset = {'#383D91':'' , '#E1E7F3':'' , '#708FC9':'' , '#F2F2F2':'' , '#FFFFFF':''}
            for line_css in f.readlines():

                if '</title>' in line_css:
                    new_line.append(line_css.replace(
                        '</title>',
                        '</title>\n'
                        '<script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>\n'
                        '<script type="text/javascript">\n'
                        '    $( document ).ready(function() {\n'
                        '                 tbl000 = $("tr td:contains(\'Обща информация за дружеството\')").parent().parent().attr("tbl","000")\n'
                        '                 tbl110 = $("tr td:contains(\'Обща информация за финансови отчети\')").parent().parent().attr("tbl","110")\n'
                        '                 tbl210 = $("tr td:contains(\'Отчет за финансовото състояние, текущо/нетекущо\')").parent().parent().attr("tbl","210")\n'
                        '                 tbl320 = $("tr td:contains(\'Отчет за всеобхватния доход, печалба или загуба, по икономически елементи\')").parent().parent().attr("tbl","320")\n'
                        '                 tbl420 = $("tr td:contains(\'Отчет за всеобхватния доход, компоненти на ОВД, представени преди данъчно облагане\')").parent().parent().attr("tbl","420")\n'
                        '                 tbl510 = $("tr td:contains(\'Отчет за паричните потоци, пряк метод\')").parent().parent().attr("tbl","510")\n'
                        '                 tbl610 = $("tr td:contains(\'Отчет за промените в собствения капитал\')").parent().parent().attr("tbl","610")\n'
                        '         $.each(["ifrs-full:NoncurrentAssets","ifrs-full:CurrentAssetsOtherThanAssetsOrDisposalGroupsClassifiedAsHeldForSaleOrAsHeldForDistributionToOwners","ifrs-full:CurrentAssets","ifrs-full:Assets","ifrs-full:EquityAttributableToOwnersOfParent","ifrs-full:Equity","ifrs-full:NoncurrentProvisions","ifrs-full:NoncurrentLiabilities","ifrs-full:CurrentProvisions","ifrs-full:CurrentLiabilitiesOtherThanLiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale","ifrs-full:CurrentLiabilities","ifrs-full:Liabilities","ifrs-full:EquityAndLiabilities","ifrs-full:ProfitLossFromOperatingActivities","ifrs-full:ProfitLossBeforeTax","ifrs-full:ProfitLossFromContinuingOperations","ifrs-full:ProfitLoss","ifrs-full:BasicEarningsLossPerShare","ifrs-full:DilutedEarningsLossPerShare","ifrs-full:OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax","ifrs-full:OtherComprehensiveIncomeBeforeTaxExchangeDifferencesOnTranslation","ifrs-full:OtherComprehensiveIncomeBeforeTaxAvailableforsaleFinancialAssets","ifrs-full:OtherComprehensiveIncomeBeforeTaxCashFlowHedges","ifrs-full:OtherComprehensiveIncomeBeforeTaxHedgesOfNetInvestmentsInForeignOperations","ifrs-full:OtherComprehensiveIncomeBeforeTaxChangeInValueOfTimeValueOfOptions","ifrs-full:OtherComprehensiveIncomeBeforeTaxChangeInValueOfForwardElementsOfForwardContracts","ifrs-full:OtherComprehensiveIncomeBeforeTaxChangeInValueOfForeignCurrencyBasisSpreads","ifrs-full:OtherComprehensiveIncomeBeforeTaxFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome","ifrs-full:OtherComprehensiveIncomeBeforeTaxInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillBeReclassifiedToProfitOrLoss","ifrs-full:OtherComprehensiveIncomeBeforeTaxFinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLoss","ifrs-full:OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossBeforeTax","ifrs-full:OtherComprehensiveIncomeBeforeTax","ifrs-full:IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLoss","ifrs-full:IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLoss","ifrs-full:OtherComprehensiveIncome","ifrs-full:ComprehensiveIncome","ifrs-full:CashFlowsFromUsedInOperations","ifrs-full:CashFlowsFromUsedInOperatingActivities","ifrs-full:CashFlowsFromUsedInInvestingActivities","ifrs-full:CashFlowsFromUsedInFinancingActivities","ifrs-full:IncreaseDecreaseInCashAndCashEquivalentsBeforeEffectOfExchangeRateChanges","ifrs-full:IncreaseDecreaseInCashAndCashEquivalents"], function( index, value ) {\n'
                        '             $("nonFraction[name=\'"+value+"\']").each(function(i) {\n'
                        '             $(this).parent().attr("style", "border-top: 1px dotted #000000; border-width: 1px; border-bottom: 1px solid black");\n'
                        '         });\n'
                        '     });\n'
                                                
                        
                        
                    '    });\n'
                    '</script>\n'
                    ))

                elif '<style type="text/css">' in line_css:
                    #new_line.append(line_css)
                    new_line.append(line_css.replace(
                        '<style type="text/css">',
                        '<style type="text/css">\n'
                        '      td {padding-top: 3px; padding-bottom:3px;}\n'
                        #'      td[style="border-left-style:none;border-right-style:none;"] {  background: #FFF; padding-top:20px;}\n'
                        
                        '      table[tbl=\'000\']>tr:nth-child(n+5)>td:not([style="border-left-style:none;border-right-style:none;"]) {background: #ebf2f3}  \n'
                        '      table[tbl=\'000\']>tr:nth-child(odd)>td:not([style="border-left-style:none;border-right-style:none;"]) {background: #FFF} \n'
                        #'      table[tbl=\'000\']>tr:nth-child(4) {display: none;}\n'
                        
                        '      table[tbl=\'110\']>tr:nth-child(n+5)>td:not([style="border-left-style:none;border-right-style:none;"]) {background: #ebf2f3}  \n'
                        '      table[tbl=\'110\']>tr:nth-child(odd)>td:not([style="border-left-style:none;border-right-style:none;"]) {background: #FFF} \n'
                        #'      table[tbl=\'110\']>tr:nth-child(4), table[tbl=\'110\']>tr:nth-child(6) {display: none;}\n'
                        
                        '      table[tbl=\'210\']>tr:nth-child(n+5)>td:not([style="border-left-style:none;border-right-style:none;"]) {background: #ebf2f3}  \n'
                        '      table[tbl=\'210\']>tr:nth-child(even)>td:not([style="border-left-style:none;border-right-style:none;"]) {background: #FFF} \n'
                        #'      table[tbl=\'210\']>tr:nth-child(4), table[tbl=\'210\']>tr:nth-child(5), table[tbl=\'210\']>tr:nth-child(6), table[tbl=\'210\']>tr:nth-child(7) {display: none;}\n'
                        
                        '      table[tbl=\'320\']>tr:nth-child(n+5)>td:not([style="border-left-style:none;border-right-style:none;"]) {background: #ebf2f3}  \n'
                        '      table[tbl=\'320\']>tr:nth-child(even)>td:not([style="border-left-style:none;border-right-style:none;"]) {background: #FFF} \n'
                        #'      table[tbl=\'320\']>tr:nth-child(4), table[tbl=\'320\']>tr:nth-child(5), table[tbl=\'320\']>tr:nth-child(6), table[tbl=\'320\']>tr:nth-child(7) {display: none;}\n'
                        
                        '      table[tbl=\'420\']>tr:nth-child(n+5)>td:not([style="border-left-style:none;border-right-style:none;"]) {background: #ebf2f3}  \n'
                        '      table[tbl=\'420\']>tr:nth-child(odd)>td:not([style="border-left-style:none;border-right-style:none;"]) {background: #FFF} \n'
                        #'      table[tbl=\'420\']>tr:nth-child(4), table[tbl=\'420\']>tr:nth-child(5), table[tbl=\'420\']>tr:nth-child(6), table[tbl=\'420\']>tr:nth-child(7) {display: none;}\n'
                        
                        '      table[tbl=\'510\']>tr:nth-child(n+5)>td:not([style="border-left-style:none;border-right-style:none;"]) {background: #ebf2f3}  \n'
                        '      table[tbl=\'510\']>tr:nth-child(odd)>td:not([style="border-left-style:none;border-right-style:none;"]) {background: #FFF} \n'
                        #'      table[tbl=\'510\']>tr:nth-child(4), table[tbl=\'510\']>tr:nth-child(5), table[tbl=\'510\']>tr:nth-child(6), table[tbl=\'510\']>tr:nth-child(7) {display: none;}\n'
                        
                        '      table[tbl=\'610\']>tr>td { border-left-color:#808080;border-left-style:solid;border-right-color:#808080;border-right-style:solid;border-top-color:#808080;border-top-style:solid;border-bottom-color:#808080;border-bottom-style:solid;}  \n'
                        #'      table:nth-child(13)>tr:nth-child(odd)>td:not([style="border-left-style:none;border-right-style:none;"]) {background: #FFF} \n'
                        '      table[tbl=\'000\']>tr>td {border-bottom: 1px solid black;}\n'
                        '      table[tbl=\'110\']>tr:nth-child(n+6) {border-bottom: 1px solid black;}\n'
                    ))
                elif 'margin:0px auto 0px auto;' in line_css:
                    #margin = line_css.replace('margin:0px auto 0px auto;','margin:0px auto 0px 0px;')
                    new_line.append(line_css.replace(
                        'margin:0px auto 0px auto;',
                        'margin:0px auto 0px 0px;'))
                elif 'height:' in line_css:
                    new_line.append(line_css.replace('height:', 'min-height:'))
                elif any(word in line_css for word in colors_reset):
                        r1 = line_css.replace('#383D91','')
                        r2 = r1.replace('#E1E7F3','')
                        r3 = r2.replace('#708FC9','')
                        r4 = r3.replace('#F2F2F2', '')
                        r5 = r4.replace('#FFFFFF', '')
                        r6 = r5.replace('calibri,sans-serif', 'Verdana')
                        r7 = r6.replace('14.667px', '12px')
                        r8 = r7.replace('border-left-color:#808080;border-left-style:solid;border-right-color:#808080;border-right-style:solid;border-top-color:#808080;border-top-style:solid;border-bottom-color:#808080;border-bottom-style:solid;',
                                        '')
                        new_line.append(r8)

                else:
                    new_line.append(line_css)
        save_path_1 = os.path.dirname(os.path.abspath(file_path))

        p = Path(file_path)
        completeName_2 = os.path.join(save_path_1,
                                      str(p.parent) + '/' + os.path.splitext(p.name)[0] + "_NEW" + p.suffix)

        with open(completeName_2, "w", encoding="utf-8") as f:
            for line in new_line:
                f.writelines(line)

        os.remove(file_path)
        os.rename(str(p.parent) + '/' + os.path.splitext(p.name)[0] + "_NEW" + p.suffix,
                  str(p.parent) + '/' + os.path.splitext(p.name)[0] + p.suffix)

        #zip_path = '/'.join(p.parts[0:-2])
        #os.rename(zip_path+'.zip', zip_path+'_old.zip')

        if file_path is not None:
            pass
    except:
        raise

    time.sleep(1.5)
    warn.destroy()
    adharbtn["state"] = "enable"
# КРАЙ НА СТЪПКА 2


# ОПЦИИ НА ЕКРАНА
step_1_labelframe = LabelFrame(
    ws,
    text='Стъпка 1')
step_1_labelframe.grid(row=0, column=0,  padx=10, pady=20, sticky=W)



label1 = Label(
    step_1_labelframe,
    text='Посочи ZIP файл:'
)
label1.grid(row=0, column=0, padx=10, pady=10, sticky=W)



zipbutton = Button(
    step_1_labelframe,
    text='Choose File',
    command=lambda: open_file_zip(zipbutton)
)
zipbutton.grid(row=0, column=1, padx=15, pady=20)






ch_label1 = Label(
    step_1_labelframe,
    text='Кои промени да се приложат:'
)
ch_label1.grid(row=1, column=0, padx=10, pady=10, sticky=W)


ch0 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="Дoбавяне на редове в CAL файла", variable=ch0).grid(row=2,column=0, padx=30, sticky=W)


ch_label1_1 = Label(
    step_1_labelframe,
    text='--------------------   ИЛИ    -----------------------'
)
ch_label1_1.grid(row=3, column=0, padx=10, pady=10, sticky=W)

ch1 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="/xbrl/2019    -->    /xbrl/2020", variable=ch1).grid(row=4,column=0, padx=30, sticky=W)

ch2 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="Taxonomy 2019    -->    Taxonomy 2020", variable=ch2).grid(row=5,column=0, padx=30, sticky=W)

ch3 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="http://xbrl.ifrs.org/taxonomy/2019-03-27/ifrs-full     -->     http://xbrl.ifrs.org/taxonomy/2020-03-16/ifrs-full",
            variable=ch3).grid(row=6,column=0, padx=30, sticky=W)



ch4 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="/xbrl.ifrs.org/taxonomy/2019-03-27/full_ifrs/full_ifrs-cor_2019-03-27.xsd   --->   /xbrl.ifrs.org/taxonomy/2020-03-16/full_ifrs/full_ifrs-cor_2020-03-16.xsd", variable=ch4).grid(row=7,column=0, padx=30, sticky=W)

ch5 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="2019-03-27   --->   2020-03-16            -      ВНИМАНИЕ, ЧУПИ ПРОВЕКАТА С ARELLE-ТО", variable=ch5).grid(row=8,column=0, padx=30, sticky=W)

ch6 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="/www.eurofiling.info/xbrl/esef/role/all/ias_1_role-110000   --->   /www.esma.europa.eu/xbrl/role/all/ias_1_role-110000", variable=ch6).grid(row=9,column=0, padx=30, sticky=W)

ch7 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="/www.eurofiling.info/xbrl/esef/role/all/ias_1_role-210000   --->   /www.esma.europa.eu/xbrl/role/all/ias_1_role-210000", variable=ch7).grid(row=10,column=0, padx=30, sticky=W)

ch8 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="/www.eurofiling.info/xbrl/esef/role/all/ias_1_role-320000   --->   /www.esma.europa.eu/xbrl/role/all/ias_1_role-320000", variable=ch8).grid(row=11,column=0, padx=30, sticky=W)

ch9 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="/www.eurofiling.info/xbrl/esef/role/all/ias_1_role-420000   --->   /www.esma.europa.eu/xbrl/role/all/ias_1_role-420000", variable=ch9).grid(row=12,column=0, padx=30, sticky=W)

ch10 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="/www.eurofiling.info/xbrl/esef/role/all/ias_7_role-510000   --->   /www.esma.europa.eu/xbrl/role/all/ias_7_role-510000", variable=ch10).grid(row=13,column=0, padx=30, sticky=W)


ch11 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="/www.eurofiling.info/xbrl/esef/role/all/ias_1_role-610000   --->   /www.esma.europa.eu/xbrl/role/all/ias_1_role-610000", variable=ch11).grid(row=14,column=0, padx=30, sticky=W)

ch12 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="preferredLabel=http://www.xbrl.org/2003/role/totalLabel   --->   Празен стринг", variable=ch12).grid(row=15,column=0, padx=30, sticky=W)

ch13 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="preferredLabel=http://www.xbrl.org/2009/role/negatedLabel   --->   Празен стринг", variable=ch13).grid(row=16,column=0, padx=30, sticky=W)

ch14 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="preferredLabel=http://www.xbrl.org/2009/role/negatedTerseLabel   --->   Празен стринг", variable=ch14).grid(row=17,column=0, padx=30, sticky=W)

ch15 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="preferredLabel=http://www.xbrl.org/2003/role/terseLabel   --->   Празен стринг", variable=ch15).grid(row=18,column=0, padx=30, sticky=W)

ch16 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="preferredLabel=http://www.xbrl.org/2003/role/periodStartLabel   --->   Празен стринг", variable=ch16).grid(row=19,column=0, padx=30, sticky=W)

ch17 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="preferredLabel=http://www.xbrl.org/2003/role/periodEndLabel   --->   Празен стринг", variable=ch17).grid(row=20,column=0, padx=30, sticky=W)

ch18 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="preferredLabel=http://www.xbrl.org/2009/role/negatedTotalLabel   --->   Празен стринг", variable=ch18).grid(row=21,column=0, padx=30, sticky=W)

ch19 = IntVar(value=1)
Checkbutton(step_1_labelframe, text="http://www.xbrl.org/2009/role/netLabel   --->   Празен стринг", variable=ch19).grid(row=22,column=0, padx=30, sticky=W)

#####################################################
#####################################################
#####################################################
#####################################################
#####################################################





#Стъпка 2 frame
step_2_labelframe = LabelFrame(
    ws,
    text='Стъпка 2')
step_2_labelframe.grid(row=2, column=0,  padx=20, pady=20, sticky=W)





adhar = Label(
    step_2_labelframe,
    text='Посочи XBRL репорт:'
)
adhar.grid(row=0, column=0, padx=50, pady=10)

adharbtn = Button(
    step_2_labelframe,
    text='Choose File',
    command=lambda: open_file_xhtml(adharbtn)
)
adharbtn.grid(row=0, column=1, padx=10, pady=20)





ws.mainloop()