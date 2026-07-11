%global tl_name ptex
%global tl_revision 77830

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A TeX system for publishing in Japanese
Group:		Publishing
URL:		https://www.ctan.org/pkg/ptex
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(cm)
Requires:	texlive(etex)
Requires:	texlive(hyphen-base)
Requires:	texlive(knuth-lib)
Requires:	texlive(plain)
Requires:	texlive(ptex-base)
Requires:	texlive(ptex-fonts)
Requires:	texlive(ptex.bin)
Requires:	texlive(uptex)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
pTeX adds features related to vertical writing, and deals with other
problems in typesetting Japanese. A manual (in both Japanese and
English) is distributed as package pTeX-manual.

