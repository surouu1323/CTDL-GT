import numpy as np

class mang:
    def __init__(self, mang):
        self.mang = mang
    def DoiXung(self):
        return all (len (row) == len (self) for row in self)
    def TamGiacTren(self):
        n = len(self)
        for i in range(1,n):
            for j in range(1, i):
                print(i ,"   " ,j," ", self[i][j])
                if self[i][j] != 0:
                    return False
        return True
    def TrungHang(self):
        n = len(self)
        for i in range (0, n):
            for j in range (i+1,n):
                a = np.array(self[i])
                b = np.array(self[j])
                if np.array_equal(a, b):
                    return True
        return False
    def NhomHang(self):
        n = len(self)
        arr = []
        for i in range (0, n):
            if i not in arr:
                print (i,end=": ")
                for j in range (i+1,n):
                    if j not in arr:
                        a = np.array(self[i])
                        b = np.array(self[j])
                        if np.array_equal(a, b):
                            arr.append(j)
                            print (j,end=" ")
                print ()          
                
class a:
  def init(self, a):
      self.a = a

  def Cong(self, b):
      new_array = []
      for num in self.a:
          result = num + b
          if result < 0 or result >= 232:
              new_array.append(-1)
          else:
              new_array.append(result)
      return new_array

  # Thêm phương thức mới để trừ một số từ mỗi phần tử của mảng
  def Tru(self, b):
      new_array = []
      for num in self.a:
          result = num - b
          if result < 0:
              new_array.append(0)  # Giả sử kết quả không thể âm
          else:
              new_array.append(result)
      return new_array

  # Thêm phương thức mới để nhân một số với mỗi phần tử của mảng
  def Nhan(self, b):
      new_array = []
      for num in self.a:
          result = num * b
          if result >= 232:
              new_array.append(-1)
          else:
              new_array.append(result)
      return new_array


arr = [123, 456, 789]  # Mảng các số nguyên không dấu
obj = a(arr)
print(obj.Cong(100))  # Kết quả không bị tràn: [223, 556, 889]