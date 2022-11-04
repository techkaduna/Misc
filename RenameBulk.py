
#bulk rename files in a given folder
import os
def main():
    i = 0
    path = "E:/TestFolder/"
    for file_name in os.listdir(path):
        
        my_dest = 'img'+str(i)+'.jpg'
        my_source = path+file_name
        my_dest = path +my_dest
        os.rename(my_source,my_dest)
        i += 1
    print('sucessful......')

def delete():
    
    path = "E:/TestFolder/"
    for file_name in os.listdir(path):
        if file_name.split('.')[-1] == 'txt':
            os.remove(path)
    print('sucessful......')

if __name__ == "__main__":
   # main()
    delete()