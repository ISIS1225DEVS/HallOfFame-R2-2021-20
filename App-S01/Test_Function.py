import config as cf
import sys
import controller
import xlsxwriter
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def TestFunction(catalog, option, data_structure, sorting_method, input_1, input_2, input_3):
    if option == 1:
        artists_sample_size = input_1
        artworks_sample_size = input_2
        catalog = controller.initCatalog(data_structure)
        controller.loadData(catalog, data_structure, artists_sample_size, artworks_sample_size)
        result = catalog

    elif option == 2:
        initial_birth_year = input_1
        end_birth_year = input_2
        requirement_info = controller.getArtistsByBirthYear(catalog, data_structure,
                                                                initial_birth_year, end_birth_year)
        elapsed_time = requirement_info[0]
        result = elapsed_time

    elif option == 3:
        initial_adquisiton_date = input_1
        end_adquisition_date = input_2
        requirement_info = controller.getArtworksByAdquisitonDate(catalog, data_structure, sorting_method,
                                                        initial_adquisiton_date, end_adquisition_date)
        elapsed_time = requirement_info[0]
        result = elapsed_time

    elif option == 4:
        artist_name = input_1
        requirement_info = controller.getArtworksByMediumAndArtist(catalog, artist_name)
        elapsed_time = requirement_info[0]
        result = elapsed_time

    elif option == 5:
        requirement_info = controller.getNationalitiesByNumArtworks(catalog, data_structure, sorting_method)
        elapsed_time = requirement_info[0]
        result = elapsed_time

    elif option == 6:  
        department = input_1
        requirement_info = controller.getTransportationCostByDepartment(catalog, data_structure, 
                                                                                sorting_method, department)
        elapsed_time = requirement_info[0]
        result = elapsed_time

    else:
        num_artists = input_1
        initial_birth_year = input_2
        end_birth_year = input_3
        requirement_info = controller.getMostProlificArtists(catalog, data_structure, sorting_method,
                                                                    initial_birth_year, end_birth_year, num_artists)
        elapsed_time = requirement_info[0]
        result = elapsed_time
    return result

def InitiateFunction():
    requeriment_test = {    2: (1900, 1905, 0),
                            3: ('1985-01-01', '2000-01-01', 0),
                            4: ('Alexei Jawlensky', 0, 0),
                            5: (0, 0, 0),
                            6: ('Drawings & Prints', 0, 0),
                            7: (3, 1900, 1905)}
    data_structure_test = { (381, 346):requeriment_test,
                            (762, 691):requeriment_test,
                            (1141, 1037):requeriment_test,
                            (1523, 1382):requeriment_test,
                            (1903, 1727):requeriment_test,
                            (2284, 2073):requeriment_test}
    Test_Data = {   'SINGLE_LINKED':data_structure_test,
                    'ARRAY_LIST':data_structure_test}


    workbook   = xlsxwriter.Workbook('Test_Data.xlsx')
    worksheet = workbook.add_worksheet()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    initial_x_position = 0
    for data_structure in Test_Data:
        data_structure_info = Test_Data[data_structure]
        initial_y_position = -9
        for sample in data_structure_info:
            input_1 = sample[0]
            input_2 = sample[1]
            print('')
            print(None, 1, data_structure, 0, input_1, input_2, 0)
            print('...')
            catalog = TestFunction(None, 1, data_structure, 0, input_1, input_2, 0)
            sample_info = data_structure_info[sample]
            initial_y_position += 1
            y_position = initial_y_position
            for requirement in sample_info:
                inputs = sample_info[requirement]
                input_1 = inputs[0]
                input_2 = inputs[1]
                input_3 = inputs[2]
                y_position += 9
                x_position_time = initial_x_position
                for sorting_method in range(1,5):
                    x_position_time += 1 
                    position_time_index = alphabet[x_position_time - 1] + str(y_position)
                    print(sample, requirement, data_structure, sorting_method, input_1, input_2, input_3)
                    elapsed_time = TestFunction(catalog, requirement, data_structure, sorting_method, input_1, input_2, input_3)
                    worksheet.write(position_time_index, elapsed_time)
        initial_x_position += 5
    workbook.close()

InitiateFunction()