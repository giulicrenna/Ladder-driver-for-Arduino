from selenium import webdriver
from lib.driver import controller
import time

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.plcfiddle.com/")


def main_function():
    output = driver.find_elements_by_css_selector("div.ote.energized")

    num = 1
    list_ = []

    def get_path(t):
        path = driver.execute_script("""gPt=function(c){
                                 if(c.id!==''){
                                     return'id("'+c.id+'")'
                                 } 
                                 if(c===document.body){
                                     return c.tagName
                                 }
                                 var a=0;
                                 var e=c.parentNode.childNodes;
                                 for(var b=0;b<e.length;b++){
                                     var d=e[b];
                                     if(d===c){
                                         return gPt(c.parentNode)+'/'+c.tagName+'['+(a+1)+']'
                                     }
                                     if(d.nodeType===1&&d.tagName===c.tagName){
                                         a++
                                     }
                                 }
                             };
                             return gPt(arguments[0]).toLowerCase();""", t)
        return path

    for i in output:
        Xpath = str(get_path(i))
        Xpath = Xpath[0:49]
        if Xpath == 'id("app-body")/div[1]/div[2]/div[2]/div[2]/div[1]':
            controller('a')
        elif Xpath == 'id("app-body")/div[1]/div[2]/div[2]/div[2]/div[2]':
            controller('b')
        elif Xpath == 'id("app-body")/div[1]/div[2]/div[2]/div[2]/div[3]':
            controller('c')
        elif Xpath == 'id("app-body")/div[1]/div[2]/div[2]/div[2]/div[4]':
            controller('d')
        elif Xpath == 'id("app-body")/div[1]/div[2]/div[2]/div[2]/div[5]':
            controller('e')
        elif Xpath == 'id("app-body")/div[1]/div[2]/div[2]/div[2]/div[6]':
            controller('f')
        elif Xpath == 'id("app-body")/div[1]/div[2]/div[2]/div[2]/div[7]':
            controller('g')
        elif Xpath == 'id("app-body")/div[1]/div[2]/div[2]/div[2]/div[8]':
            controller('h')

            
if __name__ == "__main__":  # Put main_function() in a while loop for conctant read
    while True:
        main_function()
        time.sleep(0.5)

#   id("app-body")/div[1]/div[2]/div[2]/div[2]/div[1]/div[5]/div[1]/div[1]/div[2]

#   //*[@id="app-body"]/div/div[2]/div[2]/div[2]/div[1]/div[4]/div/div/div[2]
#   //*[@id="app-body"]/div/div[2]/div[2]/div[2]/div[2]/div[4]/div/div/div[2]
#   //*[@id="app-body"]/div/div[2]/div[2]/div[2]/div[3]/div[4]/div/div/div[2]
#   //*[@id="app-body"]/div/div[2]/div[2]/div[2]/div[4]/div[4]/div/div/div[2]
#   //*[@id="app-body"]/div/div[2]/div[2]/div[2]/div[5]/div[5]/div/div/div[2]
#   //*[@id="app-body"]/div/div[2]/div[2]/div[2]/div[5]/div[6]/div/div/div[2]
#   //*[@id="app-body"]/div/div[2]/div[2]/div[2]/div[5]/div[7]/div/div/div[2]
#   //*[@id="app-body"]/div/div[2]/div[2]/div[2]/div[5]/div[8]/div/div/div[2]
