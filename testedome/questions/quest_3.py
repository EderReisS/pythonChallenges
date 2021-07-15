class MovingTotal:

    def __init__(self):
        self.list_numbers = []
        self.contains_list = set()
        self.last_pos = 0

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        self.list_numbers += numbers
        range_ = range(self.last_pos, len(self.list_numbers)-2)
        for n in range_:
            soma = sum(self.list_numbers[n:n+3])
            self.contains_list.add(soma)
            self.last_pos = n


    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        if total in self.contains_list:
            return True
        return False


if __name__ == "__main__":
    movingtotal = MovingTotal()

    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))

    movingtotal.append([5])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))

    """
    A [a1, a2, a3...]    
    B    ...
    C    ...
    D    ...
    E    ...
    
    def a (elemento):
        index = A.index(elemento)
        return B[index]
        
    
    elementos = [
     {
        "nome": "joao",
        "cidade": "recife",
    },    
    {
        "nome": "jose",
        "cidade": "caruaru",
    }, 
    ...
    ]
    
    def retorna_atributo(atributo):
        for elemento in elementos:
            print(elemento[atributo])
    
    """