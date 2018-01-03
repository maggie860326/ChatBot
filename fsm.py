from transitions.extensions import GraphMachine

count=0

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
   
    def I_am_sad(self, update):
        text = update.message.text
        if text=='/sad':
            update.message.reply_text("別擔心，我們都會幫助你的!")
            return True
        if text=='/depression_test':
            return True
        else:
            return False


    def I_am_happy(self, update):
        text = update.message.text
        return (text =='/happy')
      

    def start_question(self, update):
        text = update.message.text
        global count
        count=0
        return(text=='/start_question')

    def answer(self, update):
        text = update.message.text
        list = ['/0', '/1', '/2', '/3']
        if text in list:
            global count
            count+=list.index(text)
            print(count)
            return True
        else:
            return False
        

    def quit(self, update):
        text = update.message.text
        if text=='/quit':
           update.message.reply_text("(已退出測驗)")
           return True
        else:
           return False

    def on_enter_hi(self, update):
        update.message.reply_text("Hi\n你最近心情怎麼樣\n覺得憂鬱嗎?\n\n /happy 我心情很好~\n /sad 我有點憂鬱\n /who_are_you 你是誰?")

    def on_enter_happy(self, update):
        update.message.reply_text("太好了!\n保持心情愉快是健康的良藥喔:) \n\n如果你想進行憂鬱測驗\n可以輸入 /depression_test ")

    def on_enter_who(self, update):
        update.message.reply_text("我是可以讓你評量自身憂鬱程度的聊天機器人\n\n想知道自己的憂鬱程度\n可以輸入 /depression_test 進行測驗")

    def on_enter_intro(self, update):
        introduction = "如果你想知道自己的憂鬱情形\n可以填寫貝克憂鬱量表\n\n這是一款普遍用於測量抑鬱程度的量表，一共21題。\n\n請根據你最近的狀況，每一題選擇一個適當的選項。\n\n輸入 /start_question 開始測驗。\n\n輸入 /quit 離開。"
        update.message.reply_text(introduction)
        print("進入intro")
        

    def on_enter_Q1(self, update):
        question = "第一題\n/0 我不感到難過。\n/1 我感覺難過。\n/2 我一直覺得難過且無法振作起來。\n/3 我難過且不快樂，我不能忍受這種情形了。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q2(self, update):
        question ="第二題\n/0 對未來我並不感覺特別沮喪。\n/1 對未來我感到沮喪。\n/2 沒有任何事可讓我期盼。\n/3 我覺得未來毫無希望，並且無法改善。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q3(self, update):
        question ="第三題\n/0 我不覺得自己是個失敗者。\n/1 我比一般人害怕失敗。\n/2 回想自己的生活，我所看到的都是一大堆失敗。\n/3 我覺得自己是個徹底的失敗者。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q4(self, update):
        question ="第四題\n/0 我像過去一樣從一些事中得到滿足。\n/1 我不像過去一樣對一些事感到喜悅。\n/2 我不再從任何事中感到真正的滿足。\n/3 我對任何事都感到煩躁不滿意。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q5(self, update):
        question ="第五題\n/0 我沒有罪惡感。\n/1 偶爾我會有罪惡感。\n/2 我常常有罪惡感。\n/3 我總是感到罪惡。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q6(self, update):
        question ="第六題\n/0 我不覺得自己正在受罰。\n/1 我覺得自己可能遭受報應。\n/2 我希望受到報應。\n/3 我覺得自己正在自食惡果。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q7(self, update):
        question ="第七題\n/0 我對自己並不感到失望。\n/1 我對自己甚感失望。\n/2 我討厭自己。\n/3 我恨自己。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q8(self, update):
        question ="第八題\n/0 我不覺得自己比別人差勁。\n/1 我對自己的弱點或錯誤常常挑三揀四。\n/2 我總是為了自己的缺失苛責自己。\n/3 只要出事就會歸咎於自己。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q9(self, update):
        question ="第九題\n/0 我沒有任何想自殺的念頭。\n/1 我想自殺，但我不會真的那麼做。\n/2 我真想自殺。\n/3 如果有機會，我要自殺。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q10(self, update):
        question ="第十題\n/0 和平時比較，我哭的次數並無增加。\n/1 我現在比以前常哭。\n/2 現在我經常哭泣。\n/3 過去我還能，但現在想哭都哭不出來了。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q11(self, update):
        question ="第十一題\n/0 我對任何事並不會比以前更易動怒。\n/1 我比以前稍微有些脾氣暴躁。\n/2 很多時候我相當苦惱或脾氣暴躁。\n/3 目前我總是容易動怒。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q12(self, update):
        question ="第十二題\n/0 我關心他人。\n/1 和以前比較我有點不關心別人。\n/2 我關心別人的程度已大不如昔。\n/3 我已不再關心他人。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q13(self, update):
        question ="第十三題\n/0 我做決定能像以前一樣好。\n/1 我比以前會延後做決定的時間。\n/2 我做決定比以前更感困難。\n/3 我不再能做決定了。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q14(self, update):
        question ="第十四題\n/0 我不覺得自己比以前差勁。\n/1 我擔心自己變老或不吸引人。\n/2 我覺得自己的外表變得不再吸引人。\n/3 我認為自己長得很醜。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q15(self, update):
        question ="第十五題\n/0 我的工作情況跟以前一樣好。\n/1 我需要特別努力才能開始工作。\n/2 我必須極力催促自己才能做一些事情。\n/3 我無法做任何事。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q16(self, update):
        question ="第十六題\n/0 我像往常一樣睡得好。\n/1 我不像往常一樣睡得好。\n/2 我比往常早醒1至2小時且難再入睡。\n/3 我比往常早數小時醒來，且無法再入睡。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q17(self, update):
        question ="第十七題\n/0 我並不比以往感到疲倦。\n/1 我比以往易感到疲倦。\n/2 幾乎做任何事都令我感到疲倦。\n/3 我累得任何事都不想做。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q18(self, update):
        question ="第十八題\n/0 我的食慾不比以前差。\n/1 我的食慾不像以前那樣好。\n/2 目前我的食慾很差。\n/3 我不再感到有任何的食慾。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q19(self, update):
        question ="第十九題\n/0 我的體重並沒有下降，若有，也只有一點。\n/1 我的體重下降了2.5公斤以上。\n/2 我的體重下降了4.5公斤以上。\n/3 我的體重下降了7公斤以上。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q20(self, update):
        question ="第二十題\n/0 我並未比以往更憂慮自己的健康狀況。\n/1 我被一些生理病痛困擾，譬如胃痛、便秘等。\n/2 我很憂慮自己的健康問題，因此無法顧及許多事務。\n/3 我太憂慮自己的健康問題，以致於無法思索任何事情。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_Q21(self, update):
        question ="第二十一題\n/0 最近我對性的興趣並沒有特殊改變。\n/1 最近我對性的興趣比以前稍減。\n/2 目前我對性的興趣降低很多。\n/3 我對性已完全沒有興趣了。\n\n(或輸入 /quit 離開測驗)"
        update.message.reply_text(question)

    def on_enter_finish(self, update):
        global count
        analysis="0-13 正常範圍：表示你的情緒狀態大致平穩。 \n\n14-19 輕度憂鬱：表示你可能有輕微的情緒波動或低潮，這些低潮尚在你個人可以應付的範圍，但需要他人的關心與支持。 \n\n20-28 中度憂鬱：表示你有較多的苦腦與煩悶，情緒低潮的處理已經達到個人能夠負荷的範圍，接受專業的協助比較能協助你走出情緒的低潮。 \n\n29-63 重度憂鬱：表示你的情緒低潮可能已經達到憂鬱症的程度， 需要專業醫師的診斷再加以確立，再配合藥物治療以利復原；若有心理性因素亦需同時配合諮商治療。\n\n(輸入 /depression_test 可再次測驗)"
        update.message.reply_text("你的分數是: "+str(count)+"\n\n"+analysis)




