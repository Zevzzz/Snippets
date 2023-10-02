
import NewsPackager as nwp
import dearpygui.dearpygui as pg

# titles, contents = nwp.getContent(prompt = 'Eric', articleCount = 1, titleLength = 10, contentLength = 50)

pg.create_context()
pg.create_viewport(title='Custom Title', width=390, height=844)

with pg.window(label="Example Window"):
    pg.add_text("Number of Articles per Category")
    worldeventsSliderID = pg.add_slider_int(label="World Events", default_value = 0, max_value = 10)
    businessSliderID = pg.add_slider_int(label="Business", default_value=0, max_value=10)
    technologySliderID = pg.add_slider_int(label="Technology", default_value=0, max_value=10)
    saveButtonID = pg.add_button(label="Save")

pg.setup_dearpygui()
pg.show_viewport()



pg.start_dearpygui()
pg.destroy_context()







