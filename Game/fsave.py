import var
import const
import json

def save_init():
    try:
        file = open('Save/save.txt', 'r')
        line = file.readline()
        var.session = json.loads(line)
        file.close()

    except:
        file = open('Save/save.txt', 'w')
        file.write(json.dumps(const.empty_save))
        file.close()

        file = open('Save/save.txt', 'r')
        line = file.readline()
        var.session = json.loads(line)
        file.close()

def erase_data():
    file = open('Save/save.txt', 'w')
    file.write(json.dumps(const.empty_save))
    file.close()

    file = open('Save/save.txt', 'r')
    line = file.readline()
    var.session = json.loads(line)
    file.close()