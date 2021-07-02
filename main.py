from tkinter import *
from tkinter import END
from tkinter.ttk import *
from tkinter.filedialog import askopenfile, askopenfilename
from bs4 import BeautifulSoup, Comment
import time
import os
from datetime import date
import re

ws = Tk()
ws.title('Промяна HTML атрибути')
windowWidth = ws.winfo_reqwidth()
windowHeight = ws.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(ws.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(ws.winfo_screenheight() / 2 - windowHeight / 2)
ws.geometry("+{}+{}".format(positionRight, positionDown))


def open_file(adharbtn):
    adharbtn["state"]="disabled"
    warn = Label(
        ws,
        text='Моля, изчакайте !',
        foreground='red'
    )
    #warn.after(500, )
    warn.grid(row=1, column=0, padx=10, pady=20)
    file_path = askopenfilename()

    try:
        f = open(file_path, "r+", encoding="utf-8")




        soup = BeautifulSoup(f, 'html.parser')
        #tag = soup.find("td", string="[320000] Отчет за всеобхватния доход, печалба или загуба, по икономически елементи")
        #tag.string = "ALEKOOOOO"

        comments = soup.find_all(string=lambda text: isinstance(text, Comment))
        for c in comments:
            if '[easyESEF' in c:
                today = str(date.today())
                comment = Comment(' Изготвено за Вас на  '+today)
                c.replace_with(comment)
            if 'Col' or 'Row' or 'IXBRL VIEWER EXTENSIONS' in c:
                c = ''
        td_000000 = soup.find_all("td", text="[000000] Reporting entity")
        for td_00 in td_000000:
            td_00.string = 'Обща информация за дружеството'

        td_110000 = soup.find_all("td", text=("[110000] General information about financial statements" or "[110000] Обща информация за финансови отчети"))
        for td_11 in td_110000:
            td_11.string = 'Обща информация за финасови отчети'

        td_210000 = soup.find_all("td", text=(
                    "[210000] ‘Statement of financial position, current/non-current" or "[210000] Отчет за финансовото състояние, текущо/нетекущо"))
        for td_21 in td_210000:
            td_21.string = 'Отчет за финансовото състояние, текущо/нетекущо'

        td_220000 = soup.find_all("td", text=(
                "[220000] Statement of financial position, order of liquidity" or "[220000] Отчет за финансовото състояние, степен на ликвидност"))
        for td_22 in td_220000:
            td_22.string = 'Отчет за финансовото състояние, степен на ликвидност'

        td_310000 = soup.find_all("td", text=(
                "[310000] Statement of comprehensive income, profit or loss, by function of expense" or
                "[310000] Отчет за всеобхватния доход, печалба или загуба, по функции на разходите"))
        for td_31 in td_310000:
            td_31.string = 'Отчет за всеобхватния доход, печалба или загуба, по функции на разходите'

        td_320000 = soup.find_all("td", text= ("[320000] Statement of comprehensive income, profit or loss, by nature of expense" or "[320000] Отчет за всеобхватния доход, печалба или загуба, по икономически елементи"))
        for td_32 in td_320000:
            td_32.string = 'Отчет за всеобхватния доход, печалба или загуба, по икономически елементи'

        td_410000 = soup.find_all("td", text=(
                    "[410000] Statement of comprehensive income, OCI components presented net of tax" or
                    "[410000] Отчет за всеобхватния доход, компоненти на ОВД, представени с приспаднати данъци"))
        for td_41 in td_410000:
            td_41.string = 'Отчет за всеобхватния доход, компоненти на ОВД, представени с приспаднати данъци'

        td_420000 = soup.find_all("td", text=(
                "[420000] Statement of comprehensive income, OCI components presented before tax" or
                "[420000] Отчет за всеобхватния доход, компоненти на ОВД, представени преди данъчно облагане"))
        for td_42 in td_420000:
            td_42.string = 'Отчет за всеобхватния доход, компоненти на ОВД, представени преди данъчно облагане'

        td_510000 = soup.find_all("td", text=(
            "[510000] Отчет за паричните потоци, пряк метод" or
            "[510000] Statement of cash flows, direct method"))
        for td_51 in td_510000:
            td_51.string = 'Отчет за паричните потоци, пряк метод'

        td_520000 = soup.find_all("td", text=(
                "[520000] Отчет за паричните потоци, косвен метод" or
                "[520000] Statement of cash flows, indirect method"))
        for td_52 in td_520000:
            td_52.string = 'Отчет за паричните потоци, косвен метод'

        td_610000 = soup.find_all("td", text=(
                "[610000] Statement of changes in equity" or
                "[610000] Отчет за промените в собствения капитал"))
        for td_61 in td_610000:
            td_61.string = 'Отчет за промените в собствения капитал'



        td_total = soup.find_all("td", text=("[Total] основна нетна печалба (загуба) на акция" or
                                              "Total основна нетна печалба (загуба) на акция"))
        for td_t in td_total:
            td_t.string = 'ОБЩО основна нетна печалба (загуба) на акция'

        td_total2 = soup.find_all("td", text=('[Total] нетна печалба (загуба) на акция с намалена стойност'))
        for td_t2 in td_total2:
            td_t2.string = 'ОБЩО нетна печалба (загуба) на акция с намалена стойност'





        td_LEI = soup.find_all("td", text="LEI (Legal Entity Identifier) of reporting entity")
        for td_l in td_LEI:
            td_l.string = 'КОД: LEI (Legal Entity Identifier) на дружеството'

        td_url = soup.find_all("td", text="URL (Uniform Resource Locator) of entity web site")
        for td_u in td_url:
            td_u.string = 'URL (Uniform Resource Locator)'

        td_notes = soup.find_all("td", text="Notes")
        for td_n in td_notes:
            td_n.string = 'Бел.'

        #td_cyear = soup.find_all("td", id="_320000_D11")
        td_cyear = soup.find_all("td", text="Current Year")
        print(td_cyear)
        for td_cy in td_cyear:
            td_cy.string = 'Текуща година'

        td_pyear = soup.find_all("td", text="Previous Year")
        for td_py in td_pyear:
            td_py.string = 'Предходна година'




        td_color = soup.find_all(attrs={"style": "border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;background-color:#383D91;"})
        for cc in td_color:
            cc['style']=('border-left-style:none;border-top-style:none;border-right-style:none;border-bottom-style:none;background-color:#008000;')

        save_path = os.path.dirname(os.path.abspath(file_path))
        completeName = os.path.join(save_path, os.path.basename(file_path) + "_NEW.xhtml")
        print(completeName)
        with open(completeName, "w", encoding="utf-8") as f2:
           f2.write(soup.prettify())
        f.close()

        if file_path is not None:
            pass
    except:
        raise

    time.sleep(1.5)
    warn.destroy()
    adharbtn["state"] = "enable"



adhar = Label(
    ws,
    text='Посочи XBRL репорт:'
)
adhar.grid(row=0, column=0, padx=50, pady=10)

adharbtn = Button(
    ws,
    text='Choose File',
    command=lambda: open_file(adharbtn)
)
adharbtn.grid(row=0, column=1, padx=10, pady=20)


com1 = Label(
    ws,
    text='*Премахва коментар: Generated by [easyESEF 2019 ...... '
)
com1.grid(row=2, column=0, padx=10, pady=2 ,sticky=W)
com2 = Label(
    ws,
    text='*Сменя цвета на основните таблици от син на зелен'
)
com2.grid(row=3, column=0, padx=10, pady=2 ,sticky=W)

com3 = Label(
    ws,
    text='*Създава нов файл, на същото място, със същото име с добавено накрая _NEW'
)
com3.grid(row=4, column=0, padx=10, pady=2)



ws.mainloop()