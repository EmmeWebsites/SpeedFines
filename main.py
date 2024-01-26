from pyscript import document

def fine_calculator(speeder_name, over_speed_limit):
    '''This works out how much the fine for the speeder is. '''
    fine_costs = [630,510,400,300,230,170,120,80,30]
    speed_fine_boundaries = [45,40,35,30,25,20,15,10,1]
    
    for speed in speed_fine_boundaries:
        if over_speed_limit >= speed:
            fine = fine_costs[speed_fine_boundaries.index(speed)]
            return fine
        elif over_speed_limit <= 0:
            output3_div = document.querySelector("#output3")
            output3_div.innerText = ("{} was not speeding".format(speeder_name))

            fine = 0
            return fine

def speeder_name_checker(sentence):
    '''This checks to see if the person who was speeding is one of the people to be arrested. '''
        
    input_text = document.querySelector("#speeder_name")
    speeder_name = input_text.value

    people_to_arrest = ["james wilson", "helga norman", "zachary conroy"]
        
    for name in people_to_arrest:
        #This checks if the speeder need sto be arrested
        if name == speeder_name:
            output_div = document.querySelector("#output")
            output_div.innerText = ("This person is wanted for arrest.")
        
    return speeder_name


def main(event):

    
    speeder_name = speeder_name_checker ("speeder_name")
            

    input_text = document.querySelector("#speed_limit")
    speed_limit = input_text.value

    input_text = document.querySelector("#speeders_speed")
    speeders_speed = input_text.value


    over_speed_limit = int(speeders_speed) - int(speed_limit)
   
    fine = fine_calculator(speeder_name,over_speed_limit ) 

    output2_div = document.querySelector("#output2")
    output2_div.innerText = ("The fine for {} is ${}.".format(speeder_name,fine, over_speed_limit))