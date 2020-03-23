#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo2.py
@Time    :   2020/03/22 18:03:09
@Author  :   Vadon Mo
@Version :   1.0
@Contact :   vadonmo@126.com
@License :   Code Project Open License (CPOL)
@Desc    :   父类不参与创建，交由子类创建
'''

from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass
    pass


class PersonalSection(Section):
    def describe(self):
        print("Personal Section")
    pass


class AlbumSection(Section):
    def describe(self):
        print("Album Section")
    pass


class PatentSection(Section):
    def describe(self):
        print("Patent Section")
    pass


class PublicationSection(Section):
    def describe(self):
        print("Publication Section")
    pass


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())


class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


if __name__ == "__main__":
    profile_type = input(
        "WHich Profile you'd like to create ? [LinkedIn Or FaceBook]")
    profile = eval(profile_type.lower())()
    print("Creating Profile...", type(profile).__name__)
    print("Profile has sections --", profile.getSections())

'''
WHich Profile you'd like to create ? [LinkedIn Or FaceBook]linkedin
Creating Profile... linkedin
Profile has sections -- [<__main__.PersonalSection object at 0x00000257EF81B358>, <__main__.PatentSection object at 0x00000257EF81B400>, <__main__.PublicationSection object at 0x00000257EF81B438>]        
'''