# Telegram Chatbot
計算理論期末專題


## 介紹chatbot

[@Psychological_Test_bot](https://web.telegram.org/#/im?p=@Psychological_Test_bot) 是一款讓使用者進行心理測驗(認真)的bot
目前只有貝克憂鬱量表的測驗，以後可能會再添加其他測驗。
/depression_test 有放在bot command裡面，可從輸入欄右側點選。

### S state
1. 輸入 /depression_test ，直接跳到 [intro state](#intro-state) 進行憂鬱測驗
2. 使用者傳送任何其他訊息，跳到 [hi state](#hi-state) 打招呼

- 這個state的存在目的是為了讓使用者傳送第一則訊息後，bot能先打個招呼。原本的initial state其實是[hi state](#hi-state)，但是沒辦法在第一條訊息觸發on_enter，所以在[hi state](#hi-state)前面加一個state，使on_enter可以被觸發。



### hi state
bot會簡單問候使用者

![](https://i.imgur.com/eOWwzjY.jpg)

這時使用者如果回答:
1. /happy ，跳到 [happy state](#happy-state)
     

2. /sad，回覆「別擔心，我們會幫助你的!」，再跳到 [intro state](#intro-state) 開始測驗
![](https://i.imgur.com/sdW5l55.jpg)

3. /who_are_you 或任何其他字詞，跳到 [who state](#who-state) 讓bot自我介紹一下


### happy state

![](https://i.imgur.com/u4AkzBJ.jpg)

- 輸入 /depression_test 跳到 [intro state](#intro-state) 開始憂鬱測驗
- 輸入任何其他字詞，跳回 [hi state](#hi-state) 再次打招呼

### who state

![](https://i.imgur.com/JtqlB3Z.jpg)


- 輸入 /depression_test 跳到 [intro state](#intro-state) 開始憂鬱測驗
- 輸入任何其他字詞，跳回 [hi state](#hi-state) 再次打招呼

### intro state
介紹「貝克憂鬱量表」
測驗一共21題，每題都有四個選項，選項的數字即為分數，全部加總可得到憂鬱指數，用global變數紀錄分數。
測驗中途可以退出回到一開始的介紹，完成測驗後會顯示使用者的憂鬱指數並簡單介紹指數的意義。

![](https://i.imgur.com/3l7gCaI.jpg)

- 輸入 /start_question，global變數重設為0，跳到 [Q1 state](#qs-state) 測驗第一題
- 輸入 /quit，回覆「(已退出測驗)」，再跳回 [S state](#s-state)

### Qs state
實際上有Q1~Q21，一共21個states，每個state都是一個題目。
為了讓fsm的圖比較好理解，所以將21個states畫成一個Qs state。
用global變數紀錄分數。

![](https://i.imgur.com/8K1hQof.jpg)

- 輸入 /0, /1, /2, /3，跳到下一題的state
第21題則會跳到 [finish state](finish-state)
- 輸入 /quit，回覆「(已退出測驗)」，再跳回 [S state](#s-state)

### finish state
顯示global變數紀錄的分數，與各個分數代表的意義。

![](https://i.imgur.com/koPdgOH.jpg)

- 輸入 /depression_test 跳到 [intro state](#intro-state) 再次開始憂鬱測驗
- 輸入任何其他字詞，跳回 [hi state](#hi-state) 再次打招呼


## FSM圖

### 完整版(顯示Q1~Q21)

![](https://i.imgur.com/rojRmch.png)

### 簡化版(將Q1~Q21用Qs來代表)
因為上面的圖實在太小了看不清楚QQ

![](https://i.imgur.com/54vUSMN.png)
