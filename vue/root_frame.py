from tkinter import *

from vue.Bras_menu_frame import BrasMenuFrame
from vue.Bras_frames.subscription_frame import SubscriptionBrasFrame
from vue.Bras_frames.list_Bras_frame import ListBrasFrame
from vue.Bras_frames.profile_frame import ProfileBrasFrame
from vue.Moteur_menu_frame import MoteurMenuFrame
from vue.Moteur_frames.subscription_frame import SubscriptionMoteurFrame
from vue.Moteur_frames.list_Moteur_frame import ListMoteurFrame
from vue.Moteur_frames.profile_frame import ProfileMoteurFrame
from vue.Microcontroleur_menu_frame import MicrocontroleurMenuFrame
from vue.Microcontroleur_frames.subscription_frame import SubscriptionMicrocontroleurFrame
from vue.Microcontroleur_frames.list_Microcontroleur_frame import ListMicrocontroleurFrame
from vue.Microcontroleur_frames.profile_frame import ProfileMicrocontroleurFrame
from vue.Robot_menu_frame import RobotMenuFrame
from vue.Robot_frames.subscription_frame import SubscriptionRobotFrame
from vue.Robot_frames.list_Robot_frame import ListRobotFrame
from vue.Robot_frames.profile_frame import ProfileRobotFrame


class RootFrame(Frame):
    """
    Actions
    """

    def __init__(self, Bras_controller, Moteur_controller, Microcontroleur_controller, Robot_controller, master=None):
        super().__init__(master)
        self._Bras_controller = Bras_controller
        self._Moteur_controller = Moteur_controller
        self._Microcontroleur_controller = Microcontroleur_controller
        self._Robot_controller = Robot_controller
        self._menu_bras_frame = BrasMenuFrame(self)
        self._menu_moteur_frame = MoteurMenuFrame(self)
        self._menu_microcontroleur_frame = MicrocontroleurMenuFrame(self)
        self._menu_robot_frame = RobotMenuFrame(self)
        self._frames = []
#Partie pour les Bras
    def show_subscribe_Bras(self):
        self.hide_menu()
        # Afficher le formulaire d'ajout
        subscribe_bras_frame = SubscriptionBrasFrame(self._Bras_controller, self)
        subscribe_bras_frame.show()
        self._frames.append(subscribe_bras_frame)

    def show_Brass(self):

        # show Bras
        self.hide_menu()
        list_bras_frame = ListBrasFrame(self._Bras_controller, self)
        self._frames.append(list_bras_frame)
        list_bras_frame.show()

    def show_Bras_profile(self, Bras_id):
        Bras_data = self._Bras_controller.get_Bras(Bras_id)

        self.hide_frames()
        profile_bras_frame = ProfileBrasFrame(self._Bras_controller, Bras_data, self)
        self._frames.append(profile_bras_frame)
        profile_bras_frame.show()


# Partie Pour le Moteur
    def show_subscribe_Moteur(self):
        self.hide_menu()
        # Afficher le formulaire d'ajout
        subscribe_moteur_frame = SubscriptionMoteurFrame(self._Moteur_controller, self)
        subscribe_moteur_frame.show()
        self._frames.append(subscribe_moteur_frame)

    def show_Moteurs(self):

        # show Moteur
        self.hide_menu()
        list_moteur_frame = ListMoteurFrame(self._Moteur_controller, self)
        self._frames.append(list_moteur_frame)
        list_moteur_frame.show()

    def show_Moteur_profile(self, Moteur_id):
        Moteur_data = self._Moteur_controller.get_Moteur(Moteur_id)

        self.hide_frames()
        profile_moteur_frame = ProfileMoteurFrame(self._Moteur_controller, Moteur_data, self)
        self._frames.append(profile_moteur_frame)
        profile_moteur_frame.show()

# Partie Pour le Microcontroleur
    def show_subscribe_Microcontroleur(self):
        self.hide_menu()
        # Afficher le formulaire d'ajout
        subscribe_microcontroleur_frame = SubscriptionMicrocontroleurFrame(self._Microcontroleur_controller, self._Bras_controller,self._Moteur_controller, self)
        subscribe_microcontroleur_frame.show()
        self._frames.append(subscribe_microcontroleur_frame)

    def show_Microcontroleurs(self):

        # show Microcontroleur
        self.hide_menu()
        list_microcontroleur_frame = ListMicrocontroleurFrame(self._Microcontroleur_controller,self._Bras_controller,self._Moteur_controller, self)
        self._frames.append(list_microcontroleur_frame)
        list_microcontroleur_frame.show()

    def show_Microcontroleur_profile(self, Microcontroleur_id):
        Microcontroleur_data = self._Microcontroleur_controller.get_Microcontroleur(Microcontroleur_id)

        self.hide_frames()
        profile_microcontroleur_frame = ProfileMicrocontroleurFrame(self._Microcontroleur_controller, Microcontroleur_data, self)
        self._frames.append(profile_microcontroleur_frame)
        profile_microcontroleur_frame.show()

#Partie pour les Robot
    def show_subscribe_Robot(self):
        self.hide_menu()
        # Afficher le formulaire d'ajout
        subscribe_bras_frame = SubscriptionRobotFrame(self._Robot_controller, self)
        subscribe_bras_frame.show()
        self._frames.append(subscribe_bras_frame)

    def show_Robots(self):

        # show Robot
        self.hide_menu()
        list_robot_frame = ListRobotFrame(self._Robot_controller, self)
        self._frames.append(list_robot_frame)
        list_robot_frame.show()

    def show_Robot_profile(self, Robot_id):
        Robot_data = self._Robot_controller.get_Robot(Robot_id)

        self.hide_frames()
        profile_robot_frame = ProfileRobotFrame(self._Robot_controller, Robot_data, self)
        self._frames.append(profile_robot_frame)
        profile_robot_frame.show()


    def hide_frames(self):
        for frame in self._frames:
            frame.hide()

    def show_menu(self):
        for frame in self._frames:
            frame.destroy()
        self._frames = []
        self._menu_bras_frame.show()
        self._menu_moteur_frame.show()
        self._menu_microcontroleur_frame.show()
        self._menu_robot_frame.show()

    def hide_menu(self):
        self._menu_bras_frame.hide()
        self._menu_moteur_frame.hide()
        self._menu_microcontroleur_frame.hide()
        self._menu_robot_frame.hide()

    def back(self):
        if len(self._frames) <=1:
            self.show_menu()
            return
        last_frame = self._frames[-1]
        last_frame.destroy()
        del(self._frames[-1])
        last_frame = self._frames[-1]
        last_frame.show()

    def cancel(self):
        self.show_menu()

    def quit(self):
        self.master.destroy()
