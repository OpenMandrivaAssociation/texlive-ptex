# revision 24450
# category Package
# catalog-ctan /language/japanese/ptex
# catalog-date 2010-09-08 12:29:06 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-ptex
Version:	20100908
Release:	1
Summary:	A TeX system for publishing in Japanese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/japanese/ptex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-tex
Requires:	texlive-latex
Requires:	texlive-hyph-utf8
Requires:	texlive-adobemapping
Requires:	texlive-ipaex
Requires:	texlive-japanese
Requires:	texlive-ptex.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3
Requires(post):	texlive-tetex

%description
PTeX adds features related to vertical writing, and deals with
other problems in typesetting Japanese. A set of additions to a
TEXMF tree, for use with PTeX, may be found in package PTeX-
texmf. PTeX is distributed as WEB change files.

%pre
    %_texmf_fmtutil_pre
    %_texmf_updmap_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_fmtutil_post
    %_texmf_updmap_post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_fmtutil_pre
	%_texmf_updmap_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_fmtutil_post
	%_texmf_updmap_post
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex/morisawa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex/ptex-hiragino-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex/ptex-hiragino.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex/ptex-kozuka-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex/ptex-kozuka.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex/ptex-morisawa-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex/ptex-morisawa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex/ptex-noEmbed.map
%{_texmfdistdir}/fonts/source/ptex/ascgrp/ascgrp.mf
%{_texmfdistdir}/fonts/source/ptex/ascgrp/ascii.mf
%{_texmfdistdir}/fonts/source/ptex/ascgrp/ascii10.mf
%{_texmfdistdir}/fonts/source/ptex/ascgrp/ascii36.mf
%{_texmfdistdir}/fonts/source/ptex/jis/jis-v.pl
%{_texmfdistdir}/fonts/source/ptex/jis/jis.pl
%{_texmfdistdir}/fonts/source/ptex/nmin-ngoth/ngoth10.pl
%{_texmfdistdir}/fonts/source/ptex/nmin-ngoth/ngoth5.pl
%{_texmfdistdir}/fonts/source/ptex/nmin-ngoth/ngoth6.pl
%{_texmfdistdir}/fonts/source/ptex/nmin-ngoth/ngoth7.pl
%{_texmfdistdir}/fonts/source/ptex/nmin-ngoth/ngoth8.pl
%{_texmfdistdir}/fonts/source/ptex/nmin-ngoth/ngoth9.pl
%{_texmfdistdir}/fonts/source/ptex/nmin-ngoth/nmin10.pl
%{_texmfdistdir}/fonts/source/ptex/nmin-ngoth/nmin5.pl
%{_texmfdistdir}/fonts/source/ptex/nmin-ngoth/nmin6.pl
%{_texmfdistdir}/fonts/source/ptex/nmin-ngoth/nmin7.pl
%{_texmfdistdir}/fonts/source/ptex/nmin-ngoth/nmin8.pl
%{_texmfdistdir}/fonts/source/ptex/nmin-ngoth/nmin9.pl
%{_texmfdistdir}/fonts/source/ptex/standard/goth10.pl
%{_texmfdistdir}/fonts/source/ptex/standard/goth5.pl
%{_texmfdistdir}/fonts/source/ptex/standard/goth6.pl
%{_texmfdistdir}/fonts/source/ptex/standard/goth7.pl
%{_texmfdistdir}/fonts/source/ptex/standard/goth8.pl
%{_texmfdistdir}/fonts/source/ptex/standard/goth9.pl
%{_texmfdistdir}/fonts/source/ptex/standard/min10.pl
%{_texmfdistdir}/fonts/source/ptex/standard/min5.pl
%{_texmfdistdir}/fonts/source/ptex/standard/min6.pl
%{_texmfdistdir}/fonts/source/ptex/standard/min7.pl
%{_texmfdistdir}/fonts/source/ptex/standard/min8.pl
%{_texmfdistdir}/fonts/source/ptex/standard/min9.pl
%{_texmfdistdir}/fonts/source/ptex/standard/tgoth10.pl
%{_texmfdistdir}/fonts/source/ptex/standard/tgoth5.pl
%{_texmfdistdir}/fonts/source/ptex/standard/tgoth6.pl
%{_texmfdistdir}/fonts/source/ptex/standard/tgoth7.pl
%{_texmfdistdir}/fonts/source/ptex/standard/tgoth8.pl
%{_texmfdistdir}/fonts/source/ptex/standard/tgoth9.pl
%{_texmfdistdir}/fonts/source/ptex/standard/tmin10.pl
%{_texmfdistdir}/fonts/source/ptex/standard/tmin5.pl
%{_texmfdistdir}/fonts/source/ptex/standard/tmin6.pl
%{_texmfdistdir}/fonts/source/ptex/standard/tmin7.pl
%{_texmfdistdir}/fonts/source/ptex/standard/tmin8.pl
%{_texmfdistdir}/fonts/source/ptex/standard/tmin9.pl
%{_texmfdistdir}/fonts/tfm/ptex/ascgrp/ascgrp.tfm
%{_texmfdistdir}/fonts/tfm/ptex/ascgrp/ascii10.tfm
%{_texmfdistdir}/fonts/tfm/ptex/ascgrp/ascii36.tfm
%{_texmfdistdir}/fonts/tfm/ptex/dvips/futogo-b-v.tfm
%{_texmfdistdir}/fonts/tfm/ptex/dvips/futogo-b.tfm
%{_texmfdistdir}/fonts/tfm/ptex/dvips/futomin-b-v.tfm
%{_texmfdistdir}/fonts/tfm/ptex/dvips/futomin-b.tfm
%{_texmfdistdir}/fonts/tfm/ptex/dvips/gbm.tfm
%{_texmfdistdir}/fonts/tfm/ptex/dvips/gbmv.tfm
%{_texmfdistdir}/fonts/tfm/ptex/dvips/gtbbb-m-v.tfm
%{_texmfdistdir}/fonts/tfm/ptex/dvips/gtbbb-m.tfm
%{_texmfdistdir}/fonts/tfm/ptex/dvips/jun101-l-v.tfm
%{_texmfdistdir}/fonts/tfm/ptex/dvips/jun101-l.tfm
%{_texmfdistdir}/fonts/tfm/ptex/dvips/rml.tfm
%{_texmfdistdir}/fonts/tfm/ptex/dvips/rmlv.tfm
%{_texmfdistdir}/fonts/tfm/ptex/dvips/ryumin-l-v.tfm
%{_texmfdistdir}/fonts/tfm/ptex/dvips/ryumin-l.tfm
%{_texmfdistdir}/fonts/tfm/ptex/jis/jis-v.tfm
%{_texmfdistdir}/fonts/tfm/ptex/jis/jis.tfm
%{_texmfdistdir}/fonts/tfm/ptex/jis/jisg-v.tfm
%{_texmfdistdir}/fonts/tfm/ptex/jis/jisg.tfm
%{_texmfdistdir}/fonts/tfm/ptex/jis/jisgn-v.tfm
%{_texmfdistdir}/fonts/tfm/ptex/jis/jisgn.tfm
%{_texmfdistdir}/fonts/tfm/ptex/jis/jisn-v.tfm
%{_texmfdistdir}/fonts/tfm/ptex/jis/jisn.tfm
%{_texmfdistdir}/fonts/tfm/ptex/morisawa/FutoGoB101-Bold-H.tfm
%{_texmfdistdir}/fonts/tfm/ptex/morisawa/FutoGoB101-Bold-J.tfm
%{_texmfdistdir}/fonts/tfm/ptex/morisawa/FutoGoB101-Bold-V.tfm
%{_texmfdistdir}/fonts/tfm/ptex/morisawa/FutoMinA101-Bold-H.tfm
%{_texmfdistdir}/fonts/tfm/ptex/morisawa/FutoMinA101-Bold-J.tfm
%{_texmfdistdir}/fonts/tfm/ptex/morisawa/FutoMinA101-Bold-V.tfm
%{_texmfdistdir}/fonts/tfm/ptex/morisawa/GothicBBB-Medium-H.tfm
%{_texmfdistdir}/fonts/tfm/ptex/morisawa/GothicBBB-Medium-J.tfm
%{_texmfdistdir}/fonts/tfm/ptex/morisawa/GothicBBB-Medium-V.tfm
%{_texmfdistdir}/fonts/tfm/ptex/morisawa/Jun101-Light-H.tfm
%{_texmfdistdir}/fonts/tfm/ptex/morisawa/Jun101-Light-J.tfm
%{_texmfdistdir}/fonts/tfm/ptex/morisawa/Jun101-Light-V.tfm
%{_texmfdistdir}/fonts/tfm/ptex/morisawa/Ryumin-Light-H.tfm
%{_texmfdistdir}/fonts/tfm/ptex/morisawa/Ryumin-Light-J.tfm
%{_texmfdistdir}/fonts/tfm/ptex/morisawa/Ryumin-Light-V.tfm
%{_texmfdistdir}/fonts/tfm/ptex/nmin-ngoth/ngoth10.tfm
%{_texmfdistdir}/fonts/tfm/ptex/nmin-ngoth/ngoth5.tfm
%{_texmfdistdir}/fonts/tfm/ptex/nmin-ngoth/ngoth6.tfm
%{_texmfdistdir}/fonts/tfm/ptex/nmin-ngoth/ngoth7.tfm
%{_texmfdistdir}/fonts/tfm/ptex/nmin-ngoth/ngoth8.tfm
%{_texmfdistdir}/fonts/tfm/ptex/nmin-ngoth/ngoth9.tfm
%{_texmfdistdir}/fonts/tfm/ptex/nmin-ngoth/nmin10.tfm
%{_texmfdistdir}/fonts/tfm/ptex/nmin-ngoth/nmin5.tfm
%{_texmfdistdir}/fonts/tfm/ptex/nmin-ngoth/nmin6.tfm
%{_texmfdistdir}/fonts/tfm/ptex/nmin-ngoth/nmin7.tfm
%{_texmfdistdir}/fonts/tfm/ptex/nmin-ngoth/nmin8.tfm
%{_texmfdistdir}/fonts/tfm/ptex/nmin-ngoth/nmin9.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/goth10.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/goth5.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/goth6.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/goth7.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/goth8.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/goth9.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/min10.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/min5.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/min6.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/min7.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/min8.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/min9.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/tgoth10.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/tgoth5.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/tgoth6.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/tgoth7.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/tgoth8.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/tgoth9.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/tmin10.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/tmin5.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/tmin6.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/tmin7.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/tmin8.tfm
%{_texmfdistdir}/fonts/tfm/ptex/standard/tmin9.tfm
%{_texmfdistdir}/fonts/type1/ptex/ascgrp/ascgrp.pfb
%{_texmfdistdir}/fonts/type1/ptex/ascgrp/ascii10.pfb
%{_texmfdistdir}/fonts/type1/ptex/ascgrp/ascii36.pfb
%{_texmfdistdir}/fonts/vf/ptex/jis/jis-v.vf
%{_texmfdistdir}/fonts/vf/ptex/jis/jis.vf
%{_texmfdistdir}/fonts/vf/ptex/jis/jisg-v.vf
%{_texmfdistdir}/fonts/vf/ptex/jis/jisg.vf
%{_texmfdistdir}/fonts/vf/ptex/jis/jisgn-v.vf
%{_texmfdistdir}/fonts/vf/ptex/jis/jisgn.vf
%{_texmfdistdir}/fonts/vf/ptex/jis/jisn-v.vf
%{_texmfdistdir}/fonts/vf/ptex/jis/jisn.vf
%{_texmfdistdir}/fonts/vf/ptex/morisawa/FutoGoB101-Bold-H.vf
%{_texmfdistdir}/fonts/vf/ptex/morisawa/FutoGoB101-Bold-J.vf
%{_texmfdistdir}/fonts/vf/ptex/morisawa/FutoGoB101-Bold-V.vf
%{_texmfdistdir}/fonts/vf/ptex/morisawa/FutoMinA101-Bold-H.vf
%{_texmfdistdir}/fonts/vf/ptex/morisawa/FutoMinA101-Bold-J.vf
%{_texmfdistdir}/fonts/vf/ptex/morisawa/FutoMinA101-Bold-V.vf
%{_texmfdistdir}/fonts/vf/ptex/morisawa/GothicBBB-Medium-H.vf
%{_texmfdistdir}/fonts/vf/ptex/morisawa/GothicBBB-Medium-J.vf
%{_texmfdistdir}/fonts/vf/ptex/morisawa/GothicBBB-Medium-V.vf
%{_texmfdistdir}/fonts/vf/ptex/morisawa/Jun101-Light-H.vf
%{_texmfdistdir}/fonts/vf/ptex/morisawa/Jun101-Light-J.vf
%{_texmfdistdir}/fonts/vf/ptex/morisawa/Jun101-Light-V.vf
%{_texmfdistdir}/fonts/vf/ptex/morisawa/Ryumin-Light-H.vf
%{_texmfdistdir}/fonts/vf/ptex/morisawa/Ryumin-Light-J.vf
%{_texmfdistdir}/fonts/vf/ptex/morisawa/Ryumin-Light-V.vf
%{_texmfdistdir}/fonts/vf/ptex/nmin-ngoth/ngoth10.vf
%{_texmfdistdir}/fonts/vf/ptex/nmin-ngoth/ngoth5.vf
%{_texmfdistdir}/fonts/vf/ptex/nmin-ngoth/ngoth6.vf
%{_texmfdistdir}/fonts/vf/ptex/nmin-ngoth/ngoth7.vf
%{_texmfdistdir}/fonts/vf/ptex/nmin-ngoth/ngoth8.vf
%{_texmfdistdir}/fonts/vf/ptex/nmin-ngoth/ngoth9.vf
%{_texmfdistdir}/fonts/vf/ptex/nmin-ngoth/nmin10.vf
%{_texmfdistdir}/fonts/vf/ptex/nmin-ngoth/nmin5.vf
%{_texmfdistdir}/fonts/vf/ptex/nmin-ngoth/nmin6.vf
%{_texmfdistdir}/fonts/vf/ptex/nmin-ngoth/nmin7.vf
%{_texmfdistdir}/fonts/vf/ptex/nmin-ngoth/nmin8.vf
%{_texmfdistdir}/fonts/vf/ptex/nmin-ngoth/nmin9.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/goth10.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/goth5.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/goth6.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/goth7.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/goth8.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/goth9.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/min10.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/min5.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/min6.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/min7.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/min8.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/min9.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/tgoth10.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/tgoth5.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/tgoth6.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/tgoth7.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/tgoth8.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/tgoth9.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/tmin10.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/tmin5.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/tmin6.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/tmin7.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/tmin8.vf
%{_texmfdistdir}/fonts/vf/ptex/standard/tmin9.vf
%{_texmfdistdir}/pbibtex/bib/jxampl.bib
%{_texmfdistdir}/pbibtex/bst/jabbrv.bst
%{_texmfdistdir}/pbibtex/bst/jalpha.bst
%{_texmfdistdir}/pbibtex/bst/jipsj.bst
%{_texmfdistdir}/pbibtex/bst/jname.bst
%{_texmfdistdir}/pbibtex/bst/jorsj.bst
%{_texmfdistdir}/pbibtex/bst/jplain.bst
%{_texmfdistdir}/pbibtex/bst/junsrt.bst
%{_texmfdistdir}/pbibtex/bst/tieice.bst
%{_texmfdistdir}/pbibtex/bst/tipsj.bst
%{_texmfdistdir}/tex/platex/base/ascmac.sty
%{_texmfdistdir}/tex/platex/base/jarticle.cls
%{_texmfdistdir}/tex/platex/base/jarticle.sty
%{_texmfdistdir}/tex/platex/base/jbk10.clo
%{_texmfdistdir}/tex/platex/base/jbk11.clo
%{_texmfdistdir}/tex/platex/base/jbk12.clo
%{_texmfdistdir}/tex/platex/base/jbook.cls
%{_texmfdistdir}/tex/platex/base/jbook.sty
%{_texmfdistdir}/tex/platex/base/jltxdoc.cls
%{_texmfdistdir}/tex/platex/base/jreport.cls
%{_texmfdistdir}/tex/platex/base/jreport.sty
%{_texmfdistdir}/tex/platex/base/jsize10.clo
%{_texmfdistdir}/tex/platex/base/jsize11.clo
%{_texmfdistdir}/tex/platex/base/jsize12.clo
%{_texmfdistdir}/tex/platex/base/jt1gt.fd
%{_texmfdistdir}/tex/platex/base/jt1mc.fd
%{_texmfdistdir}/tex/platex/base/jy1gt.fd
%{_texmfdistdir}/tex/platex/base/jy1mc.fd
%{_texmfdistdir}/tex/platex/base/kinsoku.tex
%{_texmfdistdir}/tex/platex/base/nidanfloat.sty
%{_texmfdistdir}/tex/platex/base/oldpfont.sty
%{_texmfdistdir}/tex/platex/base/platex.ltx
%{_texmfdistdir}/tex/platex/base/plcore.ltx
%{_texmfdistdir}/tex/platex/base/pldefs.ltx
%{_texmfdistdir}/tex/platex/base/plext.sty
%{_texmfdistdir}/tex/platex/base/plnews.cls
%{_texmfdistdir}/tex/platex/base/ptrace.sty
%{_texmfdistdir}/tex/platex/base/tarticle.cls
%{_texmfdistdir}/tex/platex/base/tarticle.sty
%{_texmfdistdir}/tex/platex/base/tascmac.sty
%{_texmfdistdir}/tex/platex/base/tbk10.clo
%{_texmfdistdir}/tex/platex/base/tbk11.clo
%{_texmfdistdir}/tex/platex/base/tbk12.clo
%{_texmfdistdir}/tex/platex/base/tbook.cls
%{_texmfdistdir}/tex/platex/base/tbook.sty
%{_texmfdistdir}/tex/platex/base/treport.cls
%{_texmfdistdir}/tex/platex/base/treport.sty
%{_texmfdistdir}/tex/platex/base/tsize10.clo
%{_texmfdistdir}/tex/platex/base/tsize11.clo
%{_texmfdistdir}/tex/platex/base/tsize12.clo
%{_texmfdistdir}/tex/platex/config/hyphen.cfg
%{_texmfdistdir}/tex/platex/config/platex.ini
%{_texmfdistdir}/tex/ptex/base/ascii-jplain.tex
%{_texmfdistdir}/tex/ptex/base/eptex.src
%{_texmfdistdir}/tex/ptex/base/eptexdefs.lib
%{_texmfdistdir}/tex/ptex/base/kinsoku.tex
%{_texmfdistdir}/tex/ptex/base/ptex.tex
%{_texmfdistdir}/tex/ptex/config/eptex.ini
%{_texmfdistdir}/tex/ptex/config/language.def
%{_texmfdistdir}/tex/ptex/config/ptex.ini
%{_texmfdistdir}/tex/ptexgeneric/config/language.ptx
%{_texmfdistdir}/tex/ptexgeneric/hyphen/grahyph5.tex
%{_texmfdistdir}/tex/ptexgeneric/hyphen/grmhyph5.tex
%{_texmfdistdir}/tex/ptexgeneric/hyphen/grphyph5.tex
%{_texmfdistdir}/tex/ptexgeneric/hyphen/ibyhyph.tex
%_texmf_fmtutil_d/ptex
%_texmf_updmap_d/ptex
%doc %{_texmfdistdir}/doc/ptex/base/COPYRIGHT
%doc %{_texmfdistdir}/doc/ptex/base/COPYRIGHT.txt
%doc %{_texmfdistdir}/doc/ptex/base/Changes.txt
%doc %{_texmfdistdir}/doc/ptex/base/INSTALL.txt
%doc %{_texmfdistdir}/doc/ptex/base/README.txt
%doc %{_texmfdistdir}/doc/ptex/base/jfm.pdf
%doc %{_texmfdistdir}/doc/ptex/base/jfm.tex
%doc %{_texmfdistdir}/doc/ptex/base/jtex.pdf
%doc %{_texmfdistdir}/doc/ptex/base/jtex.tex
%doc %{_texmfdistdir}/doc/ptex/base/jtexdoc.pdf
%doc %{_texmfdistdir}/doc/ptex/base/jtexdoc.tex
%doc %{_texmfdistdir}/doc/ptex/base/ptexdoc.pdf
%doc %{_texmfdistdir}/doc/ptex/base/ptexdoc.tex
%doc %{_texmfdistdir}/doc/ptex/base/ptexskip.pdf
%doc %{_texmfdistdir}/doc/ptex/base/ptexskip.tex
%doc %{_texmfdistdir}/doc/ptex/jvf/COPYRIGHT
%doc %{_texmfdistdir}/doc/ptex/jvf/Changes.txt
%doc %{_texmfdistdir}/doc/ptex/jvf/README.txt
%doc %{_texmfdistdir}/doc/ptex/pbibtex/README
%doc %{_texmfdistdir}/doc/ptex/pbibtex/cpp.awk
%doc %{_texmfdistdir}/doc/ptex/pbibtex/generate.sh
%doc %{_texmfdistdir}/doc/ptex/pbibtex/jbibtex.bib
%doc %{_texmfdistdir}/doc/ptex/pbibtex/jbibtex.pdf
%doc %{_texmfdistdir}/doc/ptex/pbibtex/jbibtex.tex
%doc %{_texmfdistdir}/doc/ptex/pbibtex/jbtxbst.doc
%doc %{_texmfdistdir}/doc/ptex/pbibtex/jbtxdoc.bib
%doc %{_texmfdistdir}/doc/ptex/pbibtex/jbtxdoc.pdf
%doc %{_texmfdistdir}/doc/ptex/pbibtex/jbtxdoc.tex
%doc %{_texmfdistdir}/doc/ptex/pbibtex/jbtxhak.pdf
%doc %{_texmfdistdir}/doc/ptex/pbibtex/jbtxhak.tex
%doc %{_mandir}/man1/mendex.1*
%doc %{_texmfdir}/doc/man/man1/mendex.man1.pdf
#- source
%doc %{_texmfdistdir}/source/platex/base/Changes.txt
%doc %{_texmfdistdir}/source/platex/base/README.txt
%doc %{_texmfdistdir}/source/platex/base/README2.txt
%doc %{_texmfdistdir}/source/platex/base/Xins.ins
%doc %{_texmfdistdir}/source/platex/base/jclasses.dtx
%doc %{_texmfdistdir}/source/platex/base/jltxdoc.dtx
%doc %{_texmfdistdir}/source/platex/base/kinsoku.dtx
%doc %{_texmfdistdir}/source/platex/base/nidanfloat.dtx
%doc %{_texmfdistdir}/source/platex/base/nidanfloat.ins
%doc %{_texmfdistdir}/source/platex/base/pl209.def
%doc %{_texmfdistdir}/source/platex/base/pl209.dtx
%doc %{_texmfdistdir}/source/platex/base/pl209.ins
%doc %{_texmfdistdir}/source/platex/base/platex.dtx
%doc %{_texmfdistdir}/source/platex/base/plcls.ins
%doc %{_texmfdistdir}/source/platex/base/plcore.dtx
%doc %{_texmfdistdir}/source/platex/base/plcore.ins
%doc %{_texmfdistdir}/source/platex/base/pldoc.tex
%doc %{_texmfdistdir}/source/platex/base/pldocs.ins
%doc %{_texmfdistdir}/source/platex/base/plext.dtx
%doc %{_texmfdistdir}/source/platex/base/plfmt.ins
%doc %{_texmfdistdir}/source/platex/base/plfonts.dtx
%doc %{_texmfdistdir}/source/platex/base/plnews01.tex
%doc %{_texmfdistdir}/source/platex/base/plnews02.tex
%doc %{_texmfdistdir}/source/platex/base/plnews03.tex
%doc %{_texmfdistdir}/source/platex/base/plnews04.tex
%doc %{_texmfdistdir}/source/platex/base/plnews05.tex
%doc %{_texmfdistdir}/source/platex/base/plnews06.tex
%doc %{_texmfdistdir}/source/platex/base/plnews07.tex
%doc %{_texmfdistdir}/source/platex/base/plnews08.tex
%doc %{_texmfdistdir}/source/platex/base/plpatch.ltx
%doc %{_texmfdistdir}/source/platex/base/plvers.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/ptex <<EOF
ptex ptex - ptex.ini
eptex eptex language.def *eptex.ini
platex eptex language.ptx *platex.ini
EOF
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/ptex <<EOF
KanjiMap morisawa.map
KanjiMap ptex-@kanjiEmbed@.map
EOF
