import modules.menus as menus
import modules.clientes as clientes
import modules.admin as admins
import os

if __name__ == '__main__':
    while(True):
        os.system('clear')
        print(menus.menuMain)
        opt1 = int(input(':)'))
        match opt1:
            case 1:
                #Muestra menu para logueo de Usuarios
                while(True):
                    os.system('clear')
                    print(menus.logUser)
                    optUser1 = int(input(':)'))
                    match optUser1:
                        case 1:
                            pass
                        case 2:
                            break
                        case _:
                            input('Digite una opcion valida...')
                            os.system('clear')
            case 2:
                #Muestra menu para logueo de Administradores
                while(True):
                    os.system('clear')
                    print(menus.logAdmin)
                    optUser1 = int(input(':)'))
                    match optUser1:
                        case 1:
                            logueoAdmin = admins.loginAdmin(admins.adminInfo)
                            if(logueoAdmin):
                                while True:
                                    print(menus.optAdmin)
                                    optAd = int(input(''))
                                    match optAd:
                                        case 1:
                                            clientes.crearCliente(clientes.clientesInfo)
                                        case 2:
                                            clientes.eliminarCliente(clientes.clientesInfo)
                        case 2:
                            break
                        case _:
                            input('Digite una opcion valida...')
                            os.system('clear')
            case 3: 
                break
            case _:
                input('Digite una opcion valida...')
                os.system('clear')