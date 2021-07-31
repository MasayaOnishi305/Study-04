import pandas as pd
import datetime
import eel

RECEIPT_FILE_PATH = "./receipt/log_{datetime}.txt"
receipt_file_path=RECEIPT_FILE_PATH.format(datetime=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))

### レシート出力およびコンソール出力
def receipt(txt):
    now=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    receiptStr = '[%s: %s] %s' % ('log',now,txt)
    # ログ出力
    with open(receipt_file_path, 'a', encoding='utf-8_sig') as f:
        f.write(receiptStr + '\n')
    print(receiptStr)

#会計処理
def calc(total,payment):
    result = payment - total
    # receipt(f'合計：{total}')
    # receipt(f'お預かり：{payment}')
    # receipt(f'おつり：{result}')
    # print(f"{result}円のお釣りです。ありがとうございました。")
    log = f"--------------------\n合計：{total}\nお預かり：{payment}\nおつり：{result}"
    receipt(log)
    return(log)

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_nunber_list=[]
        self.item_master=item_master
    
    def add_item_order(self,item_code,num):
        self.item_order_list.append(item_code)
        self.item_nunber_list.append(num)

    def view_item_list(self,total):
        log = 0
        for item,num in zip(self.item_order_list,self.item_nunber_list):
            for master in self.item_master:
                if(int(item)==master.item_code):
                    subtotal = (int(num)*master.price)
                    log = f"--------------------\n商品名：{master.item_name}\n価　格：{master.price}\n注文数：{num}\n小　計：{subtotal}"
                    receipt(log)
                    #receipt("価　格：{}".format(master.price))
                    #receipt(f"注文数：{num}")
                    #receipt(f"合　計：{subtotal}")
                    total += subtotal
                else:
                    total += 0
        return  log,total
        
            
    
    
### メイン処理
def main(order_menu,quantity,total):
    try:
        df=pd.read_csv("item-master.csv")
        # マスタ登録
        item_master=[]
        item_codes=list(df["item_code"])
        item_names=list(df["item_name"])
        prices=list(df["price"])

        for item_code,item_name,price in zip(item_codes,item_names,prices):
            item_master.append(Item(item_code,item_name,price))
        
        # オーダー登録
        order=Order(item_master)
        order_num=order_menu
        num=quantity
        order.add_item_order(order_num,num)
        
        # オーダー表示
        total_price=int(total)
        result = order.view_item_list(total_price)

        return result

        #預かり金額とお釣りの計算
        #calc(total)

    except Exception as e:
        print("処理でエラーが発生しました")
    finally:
        pass



#if __name__ == "__main__":
    #main()
