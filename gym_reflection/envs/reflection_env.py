import gym
from gym import error, spaces, utils
from gym.utils import seeding

class ReflectionEnv(gym.Env):
    #metadata = {'render.modes': ['human']}
    
    def __init__(self):
        materials = ["WGT 7 0.25 ", "FSRAM45 7 0.25", "WGT_LOSSY 7 0.25", "MUR 7 0.25", "AIR 2 0", "AIR 4 0", "AIR 6 0", "AIR 8 0", "AIR 10 0", "AIR 11 0", "AIR 12 0", "AIR 15 0", "DIEL100 7 0.25", "MU_EPS_3.0 7 0.25", "EPS_2.0 7 0.25", "EPS_3.0 7 0.25", "HDF 7 0.25", "EPS_4.0 7 0.25", "QUARTZ_2 7 0.25", "WEIGHT 7 0.25", "NICALON 7 0.25", "HiK 7 0.25", "HL 7 0.25", "HL2 7 0.25", "ATK2LH 7 0.25", "ATK2TV 7 0.25"]
        self.viewer = None
        last_integral = 398
        self.observation_space = spaces.Tuple((spaces.discrete(len(materials)),
                                              spaces.Box(low=50, high=1200, shape=1),
                                              spaces.Box(low=0, high=1200, shape=1),
                                              spaces.Box(low=0, high=1200, shape=1)))
        self.action_space = spaces.Tuple((spaces.discrete(len(materials)),
                                              spaces.Box(low=50, high=1200, shape=1),
                                              spaces.Box(low=0, high=1200, shape=1),
                                              spaces.Box(low=0, high=1200, shape=1)))
        
        
        
    def step(self, action):
        
        write_action(action)
        run_physics_solver()
        s = action
        r = read_integral()
        costs = (r - last_integral)
        last_integral = r
        return s, -costs, False, {}
    
    def write_action(action):
        file_name = "salisbury.dat"
        #convert action to string
        #append string to file
        line = action.__repr__()
        line = line + "0 0"
        output_file = open(file_name, 'a')
        output_file.write(line + '\n')
        output_file.close()
        
    def run_physics_solver():
        path = r'C:\Users\SikorskyVR\Documents\Neural Network\StackWavNPEI.exe'
        location = os.path.normpath(path)
        subprocess.call([location])
        
        
    def read_integral():
        file_name = "Stack1_mag_refl_0.017453.dat"
        test_file = open(file_name, 'r')
        for line in test_file:
        for x in range(398):
            test_file.readline()
        error = test_file.readline()
        
        error = error.split()
        #y_values.append(float(error[1]))
        error =  float(error[3])
        test_file.close()
        return error
    
    def reset(self):
        last_integral = 398
        file_name = "salisbury.dat"
        full_file = open(full_file, 'w')
        full_file.write("AIR 2       0    .01    0      0        0      0\n")
        full_file.close()
    #def render(self, mode='human', close=False):