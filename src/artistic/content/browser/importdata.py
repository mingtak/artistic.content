# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from zope.component import getMultiAdapter
from plone import api
from plone import namedfile
import json
import os
import transaction
from Products.CMFPlone.utils import safe_unicode
#from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
#from zope.security import checkPermission
#from zc.relation.interfaces import ICatalog

from z3c.relationfield import RelationValue
from zope.event import notify
from zope.lifecycleevent import ObjectModifiedEvent

from plone.app.textfield.value import RichTextValue
from artistic.content.config import CITY
import logging

logger = logging.getLogger("USER SET")

citylist = {
     u"2" : u'New Taipei City',
     u"18" : u'Keelung City',
     u"1" : u'Taipei City',
     u"7" : u'Taoyuan City',
     u"8" : u'Hsinchu County',
     u"19" : u'Hsinchu City',
     u"9" : u'Miaoli County',
     u"3" :      u'Taichung City', 
     u"11" :      u'Changhua County',
     u"10" :      u'Nantou County',
     u"12" :      u'Yunlin County',
     u"20" :      u'Chiayi City', 
     u"13" :      u'Chiayi County',
     u"4" :      u'Tainan City',
     u"5" :      u'Kaohsiung City',
     u"14" :      u'Pingtung County',
     u"6" :      u'Yilan County',
     u"16" :      u'Hualien County',
     u"15" :      u'Taitung County',
     u"17" :      u'Penghu County',
     u"21" :      u'Kinmen County',
     u"22" :      u'Lienchiang County',
     u"23" : u'All Cities'}



class Import_Talent(BrowserView):

    def __call__(self):
        context = self.context
        catalog = context.portal_catalog
        portal = api.portal.get()
        with open('/home/plone/talent/talent.json', 'r') as file:
            docs = file.read()
        talent = json.loads(docs.replace('\n', '').replace('\t', ''))

        with open('/home/plone/talent/talent_county_map.json', 'r') as file:
            docs = file.read()
        talent_county_map = json.loads(docs.replace('\n', '').replace('\t', ''))

        with open('/home/plone/talent/talent_skill_map.json', 'r') as file:
            docs = file.read()
        talent_skill_map = json.loads(docs.replace('\n', '').replace('\t', ''))

        with open('/home/plone/talent/talent_stage_map.json', 'r') as file:
            docs = file.read()
        talent_stage_map = json.loads(docs.replace('\n', '').replace('\t', ''))

        with open('/home/plone/talent/talent_type_map.json', 'r') as file:
            docs = file.read()
        talent_type_map = json.loads(docs.replace('\n', '').replace('\t', ''))





        """
        hrtype = {
            u"1" : u"experts",
            u"2" : u'artist',
            u"3" : u'artsOrg',
        }

        for item in talent_type_map:
            hrObj = catalog({'Type':'HrDb', 'hrid':item['id']})[0].getObject()
            try:

#                import pdb; pdb.set_trace()
                hrObj.classfication = hrtype[str(item['type_id'])]

                notify(ObjectModifiedEvent(hrObj))
                transaction.commit()
            except:
                logger.error('匯入錯誤：%s' % hrObj.Title())



        stage = {
            u"1" : u"primary",
            u"2" : u'junior',    
            u"3" : u'senior',
        }

        for item in talent_stage_map:
            hrObj = catalog({'Type':'HrDb', 'hrid':item['id']})[0].getObject()
            try:

#                import pdb; pdb.set_trace()
                if hrObj.serviceLevel:
                    hrObj.serviceLevel.append(str(stage[str(item['stage_id'])]))
                else:
                    hrObj.serviceLevel = [stage[str(item['stage_id'])]]

               
                notify(ObjectModifiedEvent(hrObj))
                transaction.commit()
            except:
                logger.error('匯入錯誤：%s' % hrObj.Title())




        for item in talent_skill_map:
            hrObj = catalog({'Type':'HrDb', 'hrid':item['id']})[0].getObject()
            try:
                if hrObj.expertise:
                    hrObj.expertise.append('exp_%s' % str(item['skill_id']))
                else:
                    hrObj.expertise = ['exp_%s' % str(item['skill_id'])]

                notify(ObjectModifiedEvent(hrObj))
                transaction.commit()
            except:
                logger.error('匯入錯誤：%s' % hrObj.Title())


        for item in talent_county_map:
            hrObj = catalog({'Type':'HrDb', 'hrid':item['id']})[0].getObject()
            try:
                if hrObj.city:
                    hrObj.city.append(citylist[str(item['county_id'])])
                else:
                    hrObj.city = [citylist[str(item["county_id"])]]

                notify(ObjectModifiedEvent(hrObj))
                transaction.commit()
            except:
                logger.error('匯入錯誤：%s' % hrObj.Title())




        for item in talent:
            hrItem = api.content.create(
                type='HrDb',
                container=portal['hrdb'],
                hrid = item['id'],
                title=item['name'],
                artisticOrg=item['community_name'],
                serviceOrg=item['open_unit'],
                email=item['open_email'],
            )
            transaction.commit()
        """


class ModifySchoolImage(BrowserView):

    def __call__(self):
        context = self.context
        portal = api.portal.get()
        catalog = context.portal_catalog
        intIds = getUtility(IIntIds)

        brain = catalog({'Type':'SchoolInfo'})
#        import pdb; pdb.set_trace()

        for item in brain:
            try:
                obj = item.getObject()
                manager_4 = safe_unicode(obj.manager_4)
                fid = obj.imgFolderId
                for name in [fid, '%sA' % fid, '%sB' % fid, '%sC' % fid, '%sD' % fid, '%sE' % fid, '%sF' % fid]:
                    if not api.user.get(username=name):
                       continue
                    if manager_4 == safe_unicode(api.user.get(username=name).getProperty('fullname')):
                        obj.whoCanEditor = name
                        notify(ObjectModifiedEvent(obj))
                        transaction.commit()
                        break
                    else:
                        continue

#                import pdb; pdb.set_trace()
                continue
            except:pass
        return
#            if not obj.description:
#                try:
#                    obj.description = obj.Title()
#                except:pass

#            try:
#                obj.city = citylist[obj.city]
#            except:pass

#            import pdb; pdb.set_trace()
#            notify(ObjectModifiedEvent(obj))
#            transaction.commit()

        return

        for item in brain:
            obj = item.getObject()
            imgFolderId = obj.imgFolderId
#            import pdb; pdb.set_trace()
            try:
                folder = catalog({'Type':'Folder', 'id':imgFolderId})[0].getObject()
            except:continue

            for image in folder.getChildNodes():
#                import pdb; pdb.set_trace()
                if hasattr(obj.relatedImages, 'append'):
                    obj.relatedImages.append(RelationValue(intIds.getId(image)))
                else:
                    obj.relatedImages = [RelationValue(intIds.getId(image))]
#                import pdb; pdb.set_trace()
            notify(ObjectModifiedEvent(obj))
            transaction.commit()
#            import pdb; pdb.set_trace()

class ImportImageFolder(BrowserView):

    def __call__(self):
        context = self.context
        portal = api.portal.get()
        with open('/home/plone/folderList', 'r') as file:
            folderList = file.read()

        # 匯入資料夾
        """
        for folderName in folderList.split('\n'):
            api.content.create(
                type='Folder',
                container=portal['system']['images']['oldimage'],
                title=folderName,
            )
            transaction.commit()

        return
        #匯入圖檔
        for folderName in folderList.split('\n'):
            fileList = os.popen('ls /home/plone/schools_imag/%s' % folderName)
            for fileName in fileList:
                try:
                    with open('/home/plone/schools_imag/%s/%s' % (folderName, fileName.strip()), 'r') as data:
                        imageData = data.read()
                    image = api.content.create(
                        type='Image',
                        container=portal['system']['images']['oldimage'][folderName],
                        title=fileName,
                        image = namedfile.NamedBlobImage(data=imageData, filename=safe_unicode(fileName.strip()))
                    )
                    transaction.commit()
                except:
                    logger.error('匯入錯誤：%s' % fileName)
                    pass
            logger.info('已匯入：%s' % folderName) """



class ImportMembers(BrowserView):

    def __call__(self):
        context = self.context
        portal = api.portal.get()
        with open('/home/plone/school.json', 'r') as school:
            docs = school.read()
        data = json.loads(docs.replace('\n', '').replace('\t', ''))

        school = {}
        for item in data:
            school[str(item['id'])] = item["school_name"]

        with open('/home/plone/member.json', 'r') as member:
            docs = member.read()
        data = json.loads(docs.replace('\n', '').replace('\t', ''))

        userSet = []
        for item in data:

            userSet.append(u"姓名：%s\t帳號：%s\t密碼：%s" % (
                safe_unicode(item['mm_name']),
                safe_unicode(item['mm_account']),
                safe_unicode(item['mm_password'])))
        for i in userSet:
            logger.info(i)
        #import pdb; pdb.set_trace()

        """
            if item['mm_school'] == 0:
                schoolName = ''
            else:
                schoolName = school[str(item['mm_school'])]


            properties = dict(
                fullname=item['mm_name'],
                email='aec.ntnu@gmail.com',
                email2=item['mm_mail'],
                school=schoolName,
                manageTitle=item['mm_title'],
                gender=item['mm_gender'],
                tel=item['mm_tel'],
                fax=item['mm_fax'],
                mobile=item['mm_mobile'],
            )
            user = api.user.create(
                username=item['mm_account'],
                password=item['mm_password'],
                properties=properties,
            )
            transaction.commit()
            """

        return


class ImportSchools(BrowserView):

    def __call__(self):
        context = self.context
        portal = api.portal.get()
        with open('/home/plone/school.json', 'r') as school:
            docs = school.read()
        data = json.loads(docs.replace('\n', '').replace('\t', ''))

        for item in data:
            if item['stage'] == 1:
                category_1 = u'primary'
            elif item['stage'] == 2:
                category_1 = u'junior'
            elif item['stage'] == 3:
                category_1 = u'senior'
            else:
                category_1 = u'primary'

            if item['stage2'] == u'公立':
                category_2 = u'public school'
            else:
                category_2 = u'private school'

            if item['class'] == 1:
                artClassfication = u"Artistic Class"
            elif item['class'] == 2:
                artClassfication = u"Music Class"
            else:
                artClassfication = u"Dance Class"

            api.content.create(
                type='SchoolInfo',
                container=portal['artistic'],
                imgFolderId = item['school_id1'],
                title=item['school_name'],
                city=item['county'],
                category_1 = category_1,
                category_2 = category_2,
                artClassfication = artClassfication,
                schoolPhone = item['school_tel'],
                schoolFax = item['school_fax'],
                schoolAddress = item['school_address'],
                schoolDist = item['school_district'],
                schoolUrl = item['school_web'],
                principalName = item['school_principal'],
                principalExt = item['school_ext'],
                manager_1 = item['school_manage1'],
                manager_1_ext = item['school_manage1_tel'],
                manager_2 = item['school_manage2'],
                manager_2_ext = item['school_manage2_tel'],
                manager_3 = item['school_manage4'],
                manager_3_ext = item['school_manage4_tel'],
                manager_4 = item['school_manage3'],
                manager_4_ext = item['school_manage3_tel'],
                text = RichTextValue(item['introduction'], 'text/html', 'text/html')
            )

            transaction.commit()
        return
