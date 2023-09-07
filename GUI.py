import PySimpleGUI as sg
import time
import threading

def recommend_products(user_id):
    time.sleep(2)
    ans=""
    # if(user_id not in user_list):
    #     ans="(New User Detected)"+"\n"+"Top 5 recommended products for user "+user_id+" are:\n"
    #     c=0
    #     for k in top_rated_ls:
    #         ans+=k+" : "+" Avg. Rating== "+str("{:.2f}".format(top_rating_ls[c]))+"\n"
    #         c=c+1
    #     return ans
    # test_rating = {}
    # for m in test.take(100):
    #     test_rating[m["productId"].numpy()]=RankingModel()(tf.convert_to_tensor([user_id]),tf.convert_to_tensor([m["productId"]]))
    # ans="Top 5 recommended products for user "+user_id+" are:\n"
    # count=0
    # for m in sorted(test_rating, key=test_rating.get, reverse=True):
    #     temp=m.decode()
    #     ans+=temp+" : "+ str(test_rating[m].numpy()[0][0])+"\n"
    #     count=count+1
    #     if(count==5):
    #         break
    return ans

def process_and_update(user_id):
    recommended_products = recommend_products(user_id)
    window['-PROGRESS-'].update_bar(100)
    window['-OUTPUT-'].update(recommended_products)

sg.theme('Dark Blue 1')

layout = [
    [sg.Text('Enter User ID:'), sg.InputText(key='-USERID-')],
    [sg.Button('Recommend'), sg.Button('Exit')],
    [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS-')],
    [sg.Output(size=(40, 10), key='-OUTPUT-')],
]

window = sg.Window('Product Recommender', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Recommend':
        user_id = values['-USERID-']

        window['-OUTPUT-'].update('')
        window['-PROGRESS-'].update_bar(0)

        processing_thread = threading.Thread(target=process_and_update, args=(user_id,))
        processing_thread.start()

window.close()
