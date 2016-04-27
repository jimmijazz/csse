#!/usr/bin/env python3
# ##################################################################
#
#   CSSE1001/7030 - Assignment 1
#
#   Student Username: s4261634
#
#   Student Name: Joshua Bitossi
#
#   Version: 1.0.2
#
###################################################################

###################################################################
#
# The following is support code. DO NOT CHANGE.
import datetime
import time
import json

DATE_FORMAT = "%d/%m/%y %H:%M"


def time_to_time_string(time):
    """Return a string representing the supplied time

    time_to_time_string(time) -> str
    """
    dt = datetime.datetime.fromtimestamp(time)
    return dt.strftime(DATE_FORMAT)

# For use in the __str__ method for animals without tracking
BASIC_ANIMAL_FORMAT = """Animal
------
Name: {0}
Gender: {1}
Location: {2}, {3}
ID: {4}"""

# For use in the __str__ method for animals with tracking
TRACKER_ANIMAL_FORMAT = """Animal
------
Name: {0}
Gender: {1}
Location: {2}, {3}
Time: {4}
ID: {5}
Tracker ID: {6}"""

# For use in the __str__ method for plants
PLANT_FORMAT = """Plant
-----
Name: {0}
Location: {1}, {2}
ID: {3}"""


def load_model(filename):
    """Return a model built from the data in the supplied json file

    load_model(str) -> SurveyModel
    """
    with open(filename, 'r') as f:
        text = f.read()

    model_info = json.loads(text)
    model = SurveyModel()
    model.set_name(model_info['name'])
    model.set_image_file(model_info['image'])
    model.set_organisms(model_info['organisms'])
    model.set_trackers(model_info['trackers'])
    return (model)


def save_model(model, filename):


    with open(filename, 'w') as f:
        d = {'name': model.get_name(),
             'image': model.get_image_file(),
             'organisms': model.get_organism_dictionary(),
             'trackers': model.get_tracker_dictionary()
        }
        f.write(json.dumps(d, sort_keys=True,
                           indent=4, separators=(',', ': ')))

def run_GUI():
    """
    Runs the Survey GUI using this script's classes for the models.

    run_GUI() -> None
    """
    import survey

    items = list(globals().items())
    for key, value in items:
        survey.__dict__['model2'].__dict__[key] = value

    root = survey.tk.Tk()
    app = survey.SurveyApp(root)
    root.mainloop()

## End of support code
################################################################
# Write your code below
################################################################
"""
QUESTIONS FOR TUTORS
- Are the comment names for set/get survey sufficient?
- Do we include "self" in comments
- Does get full position show list of all previous locations
- Does TrackError handle/output correctly?
- Inheriting ID
- What does 'Extends organism dictionary with {'type':'plant'}' mean?
- Is string formatting too messy?
- In Animals/Plants should I use get_


TO DO
- "PLANTS - extends organism"
- ANIMALS - get TRACKING ID and TIME
- Make sure all print statements are replaced with return
- Delete TESTING Section


"""
class SurveyModel(object):
    """Contains information about the survey.
    """

    def __init__ (self):
        self._survey_name = ""  # Name of the survey
        self._organisms = {}    # {ID:Animal}
        self._trackers = {}     # Tracker information {Tracker_ID: Animal_ID}
        self._image_file = ""   # Image file name for view

    def set_name(self, name):
        """Sets the name of the survey.

        set_name(str) -> None
        """
        self._survey_name = name

    def get_name(self):
        """Returns the name of the survey.

        get_name(str) -> str
        """
        return(self._survey_name)

    def set_image_file(filename):
        """Sets the image file for the view.

        set_image_file(str) -> None
        """
        self._image_file = filename

    def get_image_file():
        """Gets the filename of the survey's image.

        get_image_file() -> str
        """
        return self._image_file

    def add_tracker(tracker_id, animal):
        """Adds tracker ID and animal ID to tracker dictionary.

        add_tracker(int,str) -> None
        """

    def add_organism(self,organism):
        """Adds an entry to the organism dictionary.

        add_organism(tuple) -> None

        """
        pass

    def get_organism_ids(self):
        """Returns a list of the keys in organism dict.

        get_organism_ids() -> list
        """
        organism_keys = []
        for key,value in self._organisms:
            organism_keys.append(key)

        return organism_keys

    def get_organism(self, organism_id):
        """Returns Organism from Organism Dictionary from given organism_id

        get_organism(organism_id) -> str
        """

    def update_location(tracker_id, position):
        pass

    def get_organism_dictionary():
        """Returns a dictionary whose keys are the keys in the organism
        dictionary and whoe values are organism objects converted to a
        dictionary.
        """

        """Assume this means dictionaries within a dictionary"""

    def get_tracker_dictionary():
        pass

    def set_organisms(dictionary):
        pass

    def set_trackers(dictionary):
        pass


class TrackError(Exception):
    """Called when tracker_id is in not a key in trackers dictionary.
    """

    def __init__(self,tracker_id):
        """Constructor: TrackError. Raises KeyError with tracker_id.

        __init__() -> KeyError
        """
        raise KeyError(tracker_id)


class Organism(object):
    """ Super class of Plant and Animal that contains information about the
    organism"""

    id_count = 0    # Count of ID's issued

    def __init__(self, position, name):
        """ Constructor: Organism

        __init___(list,str) -> None
        """

        self._position = position   # Position of Organism
        self._name = name           # Name of Organism
        Organism.id_count += 1
        self._id = 'id_'+str(Organism.id_count)   # Tracking ID of organism



    def set_id(self,id):
        """ Sets the ID of the organism. Used when loading from a file.

        set_id(str) -> None
        """

    def get_id(self):
        """Returns the ID of the object

        get_id() -> str
        """
        return self._id

    def get_position(self):
        """Returns the position of the organism. Overwritten in Animal class.

        get_position() -> list
        """
        return self._position

    def get_full_position(self):
        """Returns the position of the organism with timestamp.

        get_position() -> list
        """

    def get_name(self):
        """Returns the name of the organism

        get_name() -> str
        """
        return self._name

    def get_track(self):
        """Returns an empty list, overwritten in the Animal class.

        get_track() -> list"""
        tracking_list = []
        return tracking_list

    def to_dictionary(self):
        """Returns a dictionary of the information contained in the object.
        Extended in the Plant and Animal classes.

        to_dictionary() -> dict
        """


class Plant(Organism):
    """A representation of Organism where type is plant.
    """

    def __init__(self,position,name):
        """ Constructor: Plant.

        __init__(list,str) -> None
        """
        super().__init__(position,name)          # Inherit from Organism superclass
        self._position = position   # List of coordinates [x,y]
        self._name = name           # Plant name

    def __str__(self):
        """Returns string representation of the plant using 'PLANT_FORMAT'

        __str__() -> str
        """
        return "Plant\n-----\nName: {0}\nLocation: {1}, {2}\nID:{3}"\
        .format(self._name,self._position[0],self._position[1],self._id)

    def to_dictionary(self):
        """Returns dictionary of the information contained in the object.
        Extends organism dictionary with {'type':'plant'}

        to_dictionary() -> dictionary
        """


class Animal(Organism):
    """A representation of Organism where type is animals and position can be
    updated and listed."""

    def __init__(self, position, name, gender, tracker_id):
        """Constructor: Animal.

        __init__(list, str, str, str) -> None
        """
        super().__init__(position,name)
        self._position = position
        self._name = name
        self._gender = gender
        self._tracker_id = tracker_id

    def __str__(self):
        """Returns a string representation of the animal using
        BASIC_ANIMAL_FORMAT or TRACKER_ANIMAL_FORMAT depending on whether a
        tracker ID is supplied.

        __str__() -> str
        """
        if self._tracker_id == "":
            # Return BASIC_ANIMAL_FORMAT
            return "Animal\n \
            ------\n \
            Name: {0}\n \
            Gender: {1}\n \
            Location: {2}, {3}\n \
            ID: {4}"\
            .format(self._name,\
            self._gender,self._position[0],self._position[1],self._id)
        else:
            # Return TRACKER_ANIMAL_FORMAT
            return "Animal\n------\n \
            Name: {0}\n \
            Gender: {1}\nLocation: {2}, {3}\nTime: {4}\nID: {5}\nTracker ID: {6}".format(self._name,self._gender,self._position[0],self._position[1],time,self._id,trackerid)


    def to_dictionary(self):
        """Returns a dictionary of the information contained in the object.
        Extends organism dictionary with 'type','tracker_id' and 'gender'.

        to_dictionary() -> dict
        """

        pass

    def get_position(self):
        """Overwrites Organism class, returns xy-coordinates of current
        position.

        get_position() -> list
        """
        print( self._position)

    def add_location(self, position):
        """Adds the position and current time to position list.

        add_location(list) -> None
        """
        self._position.append([position,time_to_time_string(time.time())])


    def get_track(self):
        """List of animal positions. Returns empty list if there is only one
        entry.

        get_track(self) -> list
        """
        pass

################################################################
# TESTING - delete
################################################################

animal_1 = Animal([100,200],'buffalo','M','')
animal_1.add_location([214,100])
animal_1.get_position()

################################################################
# Write your code above
################################################################

## Uncomment the following code to automatically run the GUI
# if __name__ == '__main__':
#      run_GUI()
