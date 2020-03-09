import simplenote
import json
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env

# OR, the same with increased verbosity
# load_dotenv(verbose=True)

# settings
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

sn = simplenote.Simplenote(USER, PASSWORD)


def get_note_list():
    # listt = sn.get_note_list(data=True, since=cursor, tags=[])
    print("GETTING NOTE LIST...")
    print("--------------------")
    note_list = sn.get_note_list(data=True, tags=["links"])
    notes_json = json.dumps(note_list, indent=4)
    print(notes_json)

    with open('notes.json', 'w', encoding='utf-8') as outfile:
        json.dump(note_list, outfile)


get_note_list()


def get_note():
    """
    Gets a single note
    """
    note_id = "42f3dbe4084f4e10b4a09bc561df4689"
    note = sn.get_note(note_id)
    print("getting note ...")
    print("------------------------")
    print(json.dumps(note, indent=4))
    print("\n NOTE CONTENT")
    print("------------")
    print(note[0]['content'])


# get_note()

# CREATE NOTE
now = datetime.now()  # current date and time
date_time = now.strftime("%m/%d/%Y, %I:%M:%S%p")
# print("date and time:",date_time)

note_content = "This is a new note I created with Python!  " + date_time
note = {
    "content": note_content
}


def create_note():
    """
    CREATE NOTE
    """
    print("CREATING NOTE...")
    print("----------------")
    print(note)
    print("about to run add.note")
    sn.add_note(note)
    print("success!")


# create_note()


""" # Supports optional `tags` parameter that takes a list of tags
                                                    # to return only notes that contain at least one of these tags.
                                                    # Also supports a `since` parameter, but as per the Simperium
                                                    # API this is no longer a date, rather a cursor.
                                                    # Lastly, also supports a  `data` parameter (defaults to True)
                                                    # to only return keys/ids and versions

sn.get_note(note_id)                                # note id is value of key `key` in note dict as returned
                                                    # by get_note_list. Supports optional version integer as
                                                    # argument to return previous versions

sn.add_note(note)                                   # A ``note`` object is a dictionary with at least a
                                                    # ``content`` property, containing the note text.

sn.update_note(note)                                # The ``update_note`` method needs a note object which
                                                    # also has a ``key`` property.
sn.trash_note(note_id)

simplenote.delete_note(note_id)
"""
