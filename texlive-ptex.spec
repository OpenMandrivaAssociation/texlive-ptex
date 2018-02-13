Name:		texlive-ptex
Version:	20180128
Release:	1
Summary:	A TeX system for publishing in Japanese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/japanese/ptex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires:	texlive-tex
Requires:	texlive-latex
Requires:	texlive-hyph-utf8
Requires:	texlive-adobemapping
Requires:	texlive-ipaex
Requires:	texlive-japanese
Requires:	texlive-japanese-otf
Requires:	texlive-ptex.bin

%description
PTeX adds features related to vertical writing, and deals with
other problems in typesetting Japanese. A set of additions to a
TEXMF tree, for use with PTeX, may be found in package PTeX-
texmf. PTeX is distributed as WEB change files.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex
%_texmf_fmtutil_d/ptex
%_texmf_updmap_d/ptex
%doc %{_mandir}/man1/mendex.1*
%doc %{_texmfdistdir}/doc/man/man1/mendex.man1.pdf
%doc %{_mandir}/man1/makejvf.1*
%doc %{_texmfdistdir}/doc/man/man1/makejvf.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/ptex <<EOF
#
# from ptex:
ptex ptex - ptex.ini
eptex eptex language.def *eptex.ini
platex eptex language.dat *platex.ini
EOF
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/ptex <<EOF
KanjiMap morisawa.map
KanjiMap ptex-@kanjiEmbed@@kanjiVariant@.map
EOF
