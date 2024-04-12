from tecplotReader import *

if __name__ == "__main__":
    # input_file = 'qPot_trj.tec'
    input_file="test.plt"
    tec = TecplotFile(input_file, read_data=False)  # read data on demand

    # # test var in vars
    # data =tec.get_data_by_var_name(0,'CoordinateX')
    # # test var not in vars
    # data =tec.get_data_by_var_name(0,'Coord')

    data =tec.get_max_by_var_name(0,'CoordinateX')
    data2=tec.get_max(0,0)
    print(data,data2)
    # test var not in vars
    data =tec.get_max_by_var_name(0,'Coord')

    data =tec.get_min_by_var_name(0,'CoordinateY')
    data2=tec.get_min(0,2)
    print(data,data2)
    # test var not in vars
    data =tec.get_min_by_var_name(0,'Coord')
