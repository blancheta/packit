import vpython
from vpython import shapes, extrusion, color, vector, box, scene, rate, label, textures

rect = shapes.rectangle(width=1, height=1)
rect_side = shapes.rectangle(width=1, height=0.01)
rect_side_2 = shapes.rectangle(width=0.01, height=1)

ex = extrusion(path=[vector(0,0,0), vector(0,0.01,0)], shape=rect, color=color.red, texture=textures.stucco)
ex.pos = vector(0,0,0)

ex2 = extrusion(path=[vector(0,0,0), vector(0,1,0)], shape=rect_side, color=color.red, texture=textures.stucco)
ex2.pos = vector(-0.5,0.5,0)

ex3 = extrusion(path=[vector(0,0,0), vector(0,1,0)], shape=rect_side_2, color=color.red, texture=textures.stucco)
ex3.pos = vector(0,0.5,-0.5)

orangebox = box(color=color.orange, height=0.5, pos=vector(0, 0.25, 0))
purplebox = box(color=color.purple, height=0.5, width=0.5, length=1, pos=vector(0,0.75,0.25))
purplebox.pos.z = 2

yellowbox = box(
    color=color.yellow,
    height=0.5,
    width=0.5,
    length=0.5,
    pos=vector(-0.25,0.75,-0.25),
)
yellowbox.pos.z = 2
yellowbox.pos.x = 2

bluebox = box(color=color.blue, height=0.5, width=0.5, length=0.5, pos=vector(0.25,0.75,-0.25))
bluebox.pos.x = 2

cubic_meter = ex.width * ex2.width * ex.length
yellowbox_cubic_meter = yellowbox.height * yellowbox.width * yellowbox.length
bluebox_cubic_meter = bluebox.height * bluebox.width * bluebox.length
purplebox_cubic_meter = purplebox.height * purplebox.width * purplebox.length
greenbox_cubic_meter = orangebox.height * orangebox.width * orangebox.length

label(pos=vector(0,2,0),
    text="Available cubic meter : {} \r\n yellowbox : {} m3 \r\n bluebox: {} m3 \r\n purplebox: {} m3".format(
    cubic_meter,
    yellowbox_cubic_meter,
    bluebox_cubic_meter,
    purplebox_cubic_meter
))

def tidy_all():
    cubic_meter = ex.width * ex2.width * ex.length

    while 1:
        rate(100)
        velocity = 0.05

        if purplebox.pos.z > 0.25:
            purplebox.pos.z -= velocity

        if bluebox.pos.x > 0.25:
            bluebox.pos.x -= velocity

        if yellowbox.pos.x > -0.25 and yellowbox.pos.z > -0.25:
            yellowbox.pos.x -= velocity
            yellowbox.pos.z -= velocity

        if purplebox.pos.z < 0.25 and bluebox.pos.x < 0.25 and yellowbox.pos.x < -0.25 and yellowbox.pos.z < -0.25:
            cubic_meter = cubic_meter - ( yellowbox_cubic_meter + bluebox_cubic_meter + purplebox_cubic_meter + greenbox_cubic_meter)
            label(pos=vector(0, 2, 0),
                  text="Available cubic meter : {} m3 \r\n yellowbox : {} m3 \r\n bluebox: {} m3 \r\n purplebox: {} m3".format(
                      cubic_meter,
                      yellowbox_cubic_meter,
                      bluebox_cubic_meter,
                      purplebox_cubic_meter
                  ))
            if cubic_meter == 0:
                for o in [bluebox, purplebox, yellowbox, orangebox]:
                    o.color = color.green
            elif cubic_meter < 0:
                for o in [bluebox, purplebox, yellowbox, orangebox]:
                    o.color = color.red
            break


scene.bind("click", tidy_all)


