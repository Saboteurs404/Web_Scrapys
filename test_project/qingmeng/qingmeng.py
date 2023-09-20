import numpy as np
# 优化问题的求解
import scipy.optimize as opt

# 获取信号的相位
'''
y: 信号 (复数数组)
t0: 相对矫正的起始时间
dwell_time: 采样时间间隔
'''


def get_phase(y, t0=0, dwell_time=1):
    PAD_TO = 10000
    if len(y) < PAD_TO:
        # 对信号进行零填充
        # 用于沿指定轴连接两个或多个相同形状得数组 dtype:str 或 dtype
        y_pad = np.concatenate((y, np.zeros(PAD_TO - len(y), dtype=np.complex_)))
    else:
        y_pad = y
    '''
    对填充后的数组进行傅里叶变换，并将计算结果进行移位，使得频率的零频率位于中心位置
    '''
    # np.fft.fft()计算以为离散傅里叶变换
    fft_y = np.fft.fftshift(np.fft.fft(y_pad))

    # 对频谱进行相对矫正
    if t0 != 0:
        '''
        fft_f:计算频率轴上的频率值（以采样时间间隔为单位）
        fft_y:将频谱参数以时间便宜to为参数的旋转因子
        '''
        fft_f = np.fft.fftshift(np.fft.fftfreq(len(fft_y), dwell_time))
        fft_y *= np.exp(1j * 2 * np.pi * -t0 * fft_f)

    # 计算最小化目标函数
    '''

    目标函数的定义 是 根据 最小化傅里叶变换结果fft_y_phased的 实部平方和 和 虚部平方和的差值
    :param phi:相对矫正的角度（弧度）
    :return:
    '''

    def minf(phi):
        fft_y_phased = fft_y * np.exp(1j * phi[0])
        fft_y_phased_R2 = fft_y_phased.real ** 2
        fft_y_phased_I2 = fft_y_phased.imag ** 2
        # 选择一个阈值（最大平方幅度的1/100），将小于阈值的幅度平方设置阈值
        thresh = max(fft_y_phased_R2.max(), fft_y_phased_I2.max()) / 100
        # 返回虚部的平方 减去 实部的平方
        return np.clip(fft_y_phased_I2, thresh, None).sum() - np.clip(fft_y_phased_R2, thresh, None).sum()


    # 对频谱进行相对矫正的初始猜测
    # 通过取级大值点的的幅度（绝对值）来计算初始猜测值
    phi_guess = -np.angle(y[np.argmax(np.abs(y))])
    # 使用scipy.optimize.minimize()函数进行最小化求解
    # # 使用Nelder-Mead方法优化目标函数
    res = opt.minimize(minf, np.array([phi_guess]), method='nelder-mead')
    # 返回最小化结果中的相位值
    phi = res['x'][0]
    # 对频谱应用校正后的相位值
    # # 将频谱乘以相位值为参数的旋转因子（复数形式）
    fft_y_phased = fft_y * np.exp(1j * phi)

    # 如果校正后频谱的和小于0，则将相位值增加pi
    if fft_y_phased.sum() < 0:
        phi += np.pi
    # 返回校正后的复数数组
    return phi


# 自动相位校正
def auto_phase(y, t0=0, dwell_time=1, fast=False):
    print("1")
    if fast:
        phi = -np.angle(y[np.argmax(np.abs(y))])
    else:
        phi = get_phase(y, t0, dwell_time)
    print(2)
    # 将输入数组乘以相位值为参数的旋转因子（复数形式）
    result = y * np.exp(1j * phi)
    # 保存实部
    result_real = result.real
    result_imag = result.imag
    print(result_imag)
    print("--------------")
    print(result_real)
    print(len(result))

    # 返回校正后的复数数组
    return result


y = np.load("谢亮辉/FID.npy")
print(y)
print('------------------------------------------------------------')
auto_phase(y, t0=0, dwell_time=1, fast=False)
