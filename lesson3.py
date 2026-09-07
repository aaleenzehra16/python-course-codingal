
name=input("what is your name?")
gadget=input("what is your favourite gadget?")
agent_number=12
speed_rating=4
mission_count="three"
height=6.0
active_status=True
print("agent name",name,"and their favourite gadget is",gadget)
print(agent_number,"\n",speed_rating,"\n",mission_count,"\n",height,"\n",active_status)
print(type(agent_number),"\n",type(speed_rating),"\n",type(mission_count),"\n",type(height),"\n",type(active_status))
agent_str= str(agent_number)
speed_str=str(speed_rating)
height_str=str(height)
active_str=str(active_status)
print(type(agent_str),agent_str,"\n",type(speed_str),speed_str,"\n",type(height_str),height_str,"\n",type(active_str),active_str)
print(name[0:3])
print(name[-3:])
print(name[0:3] + name[-3:])
print(gadget[::-1])
print("name=",name,"\n","gadget=",gadget,"\n","agent number=",agent_number,"\n","speed rating",speed_rating,"\n","height",height,"\n","active status",active_status)
print("badge printing completed!")
