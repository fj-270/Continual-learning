'''import numpy as np

class OscillatoryLIFNeuron:
    """
    振荡LIF神经元：
    - 具有固有振荡频率 f0（通过内部正弦驱动电流实现）
    - 接收外部脉冲输入（加权电流）
    - 输出为LIF标准脉冲（0/1）
    """

    def __init__(self,
                 tau_m=10.0,      # 膜时间常数 (ms)
                 V_rest=-65.0,    # 静息电位 (mV)
                 V_reset=-70.0,   # 重置电位 (mV)
                 V_th=-50.0,      # 阈值电位 (mV)
                 R=10.0,          # 膜电阻 (MOhm)
                 f0=10.0,         # 固有振荡频率 (Hz)
                 A_osc=5.0,       # 振荡驱动电流幅值 (nA)
                 dt=0.1):         # 仿真步长 (ms)
        self.tau_m = tau_m
        self.V_rest = V_rest
        self.V_reset = V_reset
        self.V_th = V_th
        self.R = R
        self.f0 = f0
        self.A_osc = A_osc
        self.dt = dt

        self.V = V_rest      # 当前膜电位
        self.t = 0.0         # 内部时间（用于计算振荡相位）

    def step(self, I_syn=0.0):
        """
        推进一个时间步
        I_syn: 外部突触输入电流（来自输入脉冲加权求和得到的电流）
        返回: 是否发放脉冲 (1/0)
        """
        # 固有振荡电流：让神经元自身有一个周期性驱动
        I_osc = self.A_osc * np.sin(2 * np.pi * self.f0 * self.t / 1000.0)

        # 总输入电流 = 外部突触电流 + 自身振荡电流
        I_total = I_syn + I_osc

        # LIF膜电位更新方程
        dV = (-(self.V - self.V_rest) + self.R * I_total) / self.tau_m * self.dt
        self.V += dV

        # 判断是否发放脉冲
        spike = 0
        if self.V >= self.V_th:
            spike = 1
            self.V = self.V_reset

        # 更新内部时间
        self.t += self.dt

        return spike'''

import numpy as np
import matplotlib.pyplot as plt

# 最简单的振荡器：膜电位由一个正弦波驱动
f0 = 10        # 振荡频率 (Hz)，神经元自己的"节奏"
dt = 0.1       # 时间步长 (ms)
T = 1000       # 总仿真时间 (ms)

t = np.arange(0, T, dt)

# 核心：振荡电位 = A * sin(2*pi*f0*t)
V = np.sin(2 * np.pi * f0 * t / 1000.0)

plt.plot(t, V)
plt.xlabel("time (ms)")
plt.ylabel("oscillation value")
plt.title("最简单的振荡器")
plt.show()