from flask import Blueprint, render_template, request

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('main/index.html')


@bp.route('/feeds')
def feeds():
    return render_template('main/feeds.html')


@bp.app_template_global()
def filter_content(ctx):
    include_title = request.args.get('include_title')
    include_description = request.args.get('include_description')
    exclude_title = request.args.get('exclude_title')
    exclude_description = request.args.get('exclude_description')
    limit = request.args.get('limit', type=int)
    items = ctx['items'].copy()
    items = [item for item in items if include_title in item['title']] if include_title else items
    items = [item for item in items if include_description in item['description']] if include_description else items
    items = [item for item in items if exclude_title not in item['title']] if exclude_title else items
    items = [item for item in items if exclude_description not in item['description']] if exclude_description else items
    items = items[:limit] if limit else items
    ctx = ctx.copy()
    ctx['items'] = items
    return ctx



#---------- feed路由从这里开始 -----------#
@bp.route('/cninfo/announcement/<string:stock_id>/<string:category>')
@bp.route('/cninfo/announcement')
def cninfo_announcement(stock_id='', category=''):
    from rsshub.spiders.cninfo.announcement import ctx
    return render_template('main/atom.xml', **filter_content(ctx(stock_id,category)))


@bp.route('/chuansongme/articles/<string:category>')
@bp.route('/chuansongme/articles')
def chuansongme_articles(category=''):
    from rsshub.spiders.chuansongme.articles import ctx
    return render_template('main/atom.xml', **filter_content(ctx(category)))


@bp.route('/ctolib/topics/<string:category>')
@bp.route('/ctolib/topics')
def ctolib_topics(category=''):
    from rsshub.spiders.ctolib.topics import ctx
    return render_template('main/atom.xml', **filter_content(ctx(category)))


@bp.route('/infoq/recommend')
def infoq_recommend():
    from rsshub.spiders.infoq.recommend import ctx
    return render_template('main/atom.xml', **filter_content(ctx()))


@bp.route('/infoq/topic/<int:category>')
def infoq_topic(category=''):
    from rsshub.spiders.infoq.topic import ctx
    return render_template('main/atom.xml', **filter_content(ctx(category)))


@bp.route('/dxzg/notice')
def dxzg_notice():
    from rsshub.spiders.dxzg.notice import ctx
    return render_template('main/atom.xml', **filter_content(ctx()))


@bp.route('/earningsdate/prnewswire')
def earningsdate_prnewswire():
    from rsshub.spiders.earningsdate.prnewswire import ctx
    return render_template('main/atom.xml', **filter_content(ctx()))

@bp.route('/earningsdate/globenewswire')
def earningsdate_globenewswire():
    from rsshub.spiders.earningsdate.globenewswire import ctx
    return render_template('main/atom.xml', **filter_content(ctx()))

@bp.route('/earningsdate/businesswire')
def earningsdate_businesswire():
    from rsshub.spiders.earningsdate.businesswire import ctx
    return render_template('main/atom.xml', **filter_content(ctx()))

@bp.route('/jiemian/newsflash/<string:category>')
def jiemian_newsflash(category=''):
    from rsshub.spiders.jiemian.newsflash import ctx
    return render_template('main/atom.xml', **filter_content(ctx(category)))

@bp.route('/csrc/audit/<string:category>')
def csrc_audit(category=''):
    from rsshub.spiders.csrc.audit import ctx
    return render_template('main/atom.xml', **filter_content(ctx(category)))

@bp.route('/caixin/scroll/<string:category>')
def caixin_scroll(category=''):
    from rsshub.spiders.caixin.scroll import ctx
    return render_template('main/atom.xml', **filter_content(ctx(category)))    

@bp.route('/eastmoney/report/<string:type>/<string:category>')
def eastmoney_report(category='', type=''):
    from rsshub.spiders.eastmoney.report import ctx
    return render_template('main/atom.xml', **filter_content(ctx(type,category)))      

@bp.route('/xuangubao/<string:type>/<string:category>')
def xuangubao_xuangubao(type='', category=''):
    from rsshub.spiders.xuangubao.xuangubao import ctx
    return render_template('main/atom.xml', **filter_content(ctx(type, category)))        

@bp.route('/cls/subject/<string:category>')
def cls_subject(category=''):
    from rsshub.spiders.cls.subject import ctx
    return render_template('main/atom.xml', **filter_content(ctx(category)))      

@bp.route('/chaindd/column/<string:category>')
def chaindd_column(category=''):
    from rsshub.spiders.chaindd.column import ctx
    return render_template('main/atom.xml', **filter_content(ctx(category)))      

@bp.route('/techcrunch/tag/<string:category>')
def techcrunch_tag(category=''):
    from rsshub.spiders.techcrunch.tag import ctx
    return render_template('main/atom.xml', **filter_content(ctx(category)))

@bp.route('/weiyangx/home')
def weiyangx_home():
    from rsshub.spiders.weiyangx.home import ctx
    return render_template('main/atom.xml', **filter_content(ctx()))

@bp.route('/weiyangx/express/')
def weiyangx_express():
    from rsshub.spiders.weiyangx.express import ctx
    return render_template('main/atom.xml', **filter_content(ctx()))

@bp.route('/weiyangx/tag/<string:category>')
def weiyangx_tag(category=''):
    from rsshub.spiders.weiyangx.tag import ctx
    return render_template('main/atom.xml', **filter_content(ctx(category)))

@bp.route('/jintiankansha/column/<string:category>')
def jintiankansha_column(category=''):
    from rsshub.spiders.jintiankansha.column import ctx
    return render_template('main/atom.xml', **filter_content(ctx(category)))    

@bp.route('/interotc/cpgg/<string:category>')
def interotc_cpgg(category=''):
    from rsshub.spiders.interotc.cpgg import ctx
    return render_template('main/atom.xml', **filter_content(ctx(category)))    

@bp.route('/benzinga/ratings/<string:category>')
def benzinga_ratings(category=''):
    from rsshub.spiders.benzinga.ratings import ctx
    return render_template('main/atom.xml', **filter_content(ctx(category)))        