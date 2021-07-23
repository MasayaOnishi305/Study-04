import pandas as pd

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

    def view_item_list(self):
        total = 0
        for item,num in zip(self.item_order_list,self.item_nunber_list):
            for master in self.item_master:
                if(int(item)==master.item_code):
                    subtotal = (int(num)*master.price)
                    print("商品名：{}".format(master.item_name))
                    print("価　格：{}".format(master.price))
                    print(f"注文数：{num}")
                    print(f"合　計：{subtotal}")
                    total += subtotal
                else:
                    total += 0
        return  total


    def calc(self,total):
        while True:
            money = int(input("お預かり金額を入力してください："))
            if(total > money):
                print('金額が足りません。お預かり金額の入力からやり直してください')
            else:
                break
        result = money - total
        print(f"{result}円のお釣りです。ありがとうございました。")
        
            
    
    
### メイン処理
def main():
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
        order_num=input("オーダー番号を入力してください:")
        num=input(f"{order_num}の注文数を入力してください:")
        order.add_item_order(order_num,num)
        
        # オーダー表示
        total = order.view_item_list()

        #預かり金額とお釣りの計算
        order.calc(total)
    except Exception as e:
        print("処理でエラーが発生しました")
    finally:
        pass

    
if __name__ == "__main__":
    main()
