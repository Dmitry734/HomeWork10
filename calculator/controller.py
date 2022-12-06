import viewer as vr
import Operation as rt


def button_click(flag):
    first_numb, second_numb, numb_oper = vr.menu_collection(flag)
    res = rt.calc(first_numb, second_numb, numb_oper)
    vr.view_res(flag, res)
