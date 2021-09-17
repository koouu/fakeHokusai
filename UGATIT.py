
from dataset import ImageFolder
from torchvision import transforms
#from torch.utils.data import DataLoader
#from networks import *
from utils import *
from glob import glob

class UGATIT(object) :
    def __init__(self):
        self.light = True
        self.model_name = 'UGATIT'
        
        self.ch=64
        
        """ Generator """
        self.n_res = 4
        
        self.dataset="picture2art"
        self.result_dir="results"
        self.img_size = 256
        self.img_ch = 3

        self.device = "cpu"
        
        
        print("__init__finished")
        
    def test(self):
        print("fas")
    ##################################################################################
    # Model
    ##################################################################################
    """
    def build_model(self):
        
        
        self.genA2B = ResnetGenerator(input_nc=3, output_nc=3, ngf=self.ch, n_blocks=self.n_res, img_size=self.img_size, light=self.light).to(self.device)
        
        
        
        
        

    
    def load(self):
        params = torch.load(os.path.join('model','HokusaiAI.pt'))
        self.genA2B.load_state_dict(params['genA2B'])
        #print(self.genA2B.is_cuda)
        

    def test(self,image_name):
        
        model_list = glob(os.path.join('model', 'HokusaiAI.pt'))
        
        print(torch.__version__)
        
        



        if not len(model_list) == 0:
            self.load()
            print(" [*] Load SUCCESS")
        else:
            print(" [*] Load FAILURE")
            return

        self.genA2B.eval()#, self.genB2A.eval()
        
        
        test_transform = transforms.Compose([
            transforms.Resize((self.img_size, self.img_size)),
            transforms.ToTensor(),
            transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
        ])
        
        testA = ImageFolder(os.path.join('static','images','download'), test_transform)
        
        testA_loader = DataLoader(testA, batch_size=1, shuffle=False)
        
        ""
        real_A = real_A.to(self.device)

        fake_A2B, _, fake_A2B_heatmap = self.genA2B(real_A)
        
        A2B = np.concatenate((RGB2BGR(tensor2numpy(denorm(real_A[0]))),
                                  RGB2BGR(tensor2numpy(denorm(fake_A2B[0])))), 0)

        cv2.imwrite(os.path.join(self.result_dir, self.dataset, 'test', 'Base_%d.png' % (n + 1)), RGB2BGR(tensor2numpy(denorm(real_A[0]))) * 255.0)
            
        cv2.imwrite(os.path.join(self.result_dir, self.dataset, 'test', 'A2B_%d.png' % (n + 1)), RGB2BGR(tensor2numpy(denorm(fake_A2B[0]))) * 255.0)
        ""
        for n, (real_A, _) in enumerate(testA_loader):
            real_A = real_A.to(self.device)
            print(type(real_A))
            fake_A2B, _, _ = self.genA2B(real_A)
            ""
            fake_A2B2A, _, fake_A2B2A_heatmap = self.genB2A(fake_A2B)

            fake_A2A, _, fake_A2A_heatmap = self.genB2A(real_A)
            ""
            A2B = np.concatenate((RGB2BGR(tensor2numpy(denorm(real_A[0]))),
                                  RGB2BGR(tensor2numpy(denorm(fake_A2B[0])))), 0)

            
            cv2.imwrite(os.path.join('static','images','upload', image_name), RGB2BGR(tensor2numpy(denorm(fake_A2B[0]))) * 255.0)
            
    """
        
