import pywebify.Web as web
from pywebify.Widgets import Label


website = web.NewSite()

# Home page
home_page = web.NewPage(website, "__main__")
home_page.set_title("Hello, World!")

label1 = Label(home_page, "This is test")
label2 = Label(home_page, "This is a second test")
label3 = Label(home_page, "This is a third test")

website._testloop()

#website.mainloop()