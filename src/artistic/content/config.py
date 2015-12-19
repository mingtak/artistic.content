# -*- coding: utf-8 -*-
from artistic.content import _
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


# 專業領域
EXPERTISE = SimpleVocabulary(
    [SimpleTerm(value=u'exp_01', title=_(u'help_exp_01')),
     SimpleTerm(value=u'exp_02', title=_(u'help_exp_02')),
     SimpleTerm(value=u'exp_03', title=_(u'help_exp_03')),
     SimpleTerm(value=u'exp_04', title=_(u'help_exp_04')),
     SimpleTerm(value=u'exp_05', title=_(u'help_exp_05')),
     SimpleTerm(value=u'exp_06', title=_(u'help_exp_06')),
     SimpleTerm(value=u'exp_07', title=_(u'help_exp_07')),
     SimpleTerm(value=u'exp_08', title=_(u'help_exp_08')),
     SimpleTerm(value=u'exp_09', title=_(u'help_exp_09')),
     SimpleTerm(value=u'exp_10', title=_(u'help_exp_10')),
     SimpleTerm(value=u'exp_11', title=_(u'help_exp_11')),
     SimpleTerm(value=u'exp_12', title=_(u'help_exp_12')),
     SimpleTerm(value=u'exp_13', title=_(u'help_exp_13')),
     SimpleTerm(value=u'exp_14', title=_(u'help_exp_14')),
     SimpleTerm(value=u'exp_15', title=_(u'help_exp_15')),
     SimpleTerm(value=u'exp_16', title=_(u'help_exp_16')),
     SimpleTerm(value=u'exp_17', title=_(u'help_exp_17')),
     SimpleTerm(value=u'exp_18', title=_(u'help_exp_18')),
     SimpleTerm(value=u'exp_19', title=_(u'help_exp_19')),
     SimpleTerm(value=u'exp_20', title=_(u'help_exp_20')),
     SimpleTerm(value=u'exp_21', title=_(u'help_exp_21')),
     SimpleTerm(value=u'exp_22', title=_(u'help_exp_22')),
     SimpleTerm(value=u'exp_23', title=_(u'help_exp_23')),
     SimpleTerm(value=u'exp_24', title=_(u'help_exp_24')),
     SimpleTerm(value=u'exp_25', title=_(u'help_exp_25')),
     SimpleTerm(value=u'exp_26', title=_(u'help_exp_26')),
     SimpleTerm(value=u'exp_27', title=_(u'help_exp_27')),
     SimpleTerm(value=u'exp_28', title=_(u'help_exp_28')),
     SimpleTerm(value=u'exp_29', title=_(u'help_exp_29')),
     SimpleTerm(value=u'exp_30', title=_(u'help_exp_30')),
     SimpleTerm(value=u'exp_31', title=_(u'help_exp_31')),
     SimpleTerm(value=u'exp_32', title=_(u'help_exp_32')),
     SimpleTerm(value=u'exp_33', title=_(u'help_exp_33')),
     SimpleTerm(value=u'exp_34', title=_(u'help_exp_34')),
     SimpleTerm(value=u'exp_35', title=_(u'help_exp_35')),
     SimpleTerm(value=u'exp_36', title=_(u'help_exp_36')),
     SimpleTerm(value=u'exp_37', title=_(u'help_exp_37')),]
    )

# 服務教育階段
SERVICE_LEVEL = SimpleVocabulary(
    [SimpleTerm(value=u'primary', title=_(u'primary')),
     SimpleTerm(value=u'junior', title=_(u'junior')),
     SimpleTerm(value=u'senior', title=_(u'senior'))]
    )

# 人才類別
HR_CLASSFICATION = SimpleVocabulary(
    [SimpleTerm(value=u'experts', title=_(u'experts')),
     SimpleTerm(value=u'artist', title=_(u'artist')),
     SimpleTerm(value=u'artsOrg', title=_(u'artOrg'))]
    )

# 縣市別
CITY = SimpleVocabulary(
    [SimpleTerm(value=u'All Cities', title=_(u'All Cities')),
     SimpleTerm(value=u'New Taipei City', title=_(u'New Taipei City')),
     SimpleTerm(value=u'Keelung City', title=_(u'Keelung City')),
     SimpleTerm(value=u'Taipei City', title=_(u'Taipei City')),
     SimpleTerm(value=u'Taoyuan City', title=_(u'Taoyuan City')),
     SimpleTerm(value=u'Hsinchu County', title=_(u'Hsinchu County')),
     SimpleTerm(value=u'Hsinchu City', title=_(u'Hsinchu City')),
     SimpleTerm(value=u'Miaoli County', title=_(u'Miaoli County')),
     SimpleTerm(value=u'Taichung City', title=_(u'Taichung City')),
     SimpleTerm(value=u'Changhua County', title=_(u'Changhua County')),
     SimpleTerm(value=u'Nantou County', title=_(u'Nantou County')),
     SimpleTerm(value=u'Yunlin County', title=_(u'Yunlin County')),
     SimpleTerm(value=u'Chiayi City', title=_(u'Chiayi City')),
     SimpleTerm(value=u'Chiayi County', title=_(u'Chiayi County')),
     SimpleTerm(value=u'Tainan City', title=_(u'Tainan City')),
     SimpleTerm(value=u'Kaohsiung City', title=_(u'Kaohsiung City')),
     SimpleTerm(value=u'Pingtung County', title=_(u'Pingtung County')),
     SimpleTerm(value=u'Yilan County', title=_(u'Yilan County')),
     SimpleTerm(value=u'Hualien County', title=_(u'Hualien County')),
     SimpleTerm(value=u'Taitung County', title=_(u'Taitung County')),
     SimpleTerm(value=u'Penghu County', title=_(u'Penghu County')),
     SimpleTerm(value=u'Kinmen County', title=_(u'Kinmen County')),
     SimpleTerm(value=u'Lienchiang County', title=_(u'Lienchiang County')),]
     )
