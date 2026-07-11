%global tl_name superiors
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Attach superior figures to a font family
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/superiors
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/superiors.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/superiors.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the attachment of an arbitrary superior figures font
to a font family that lacks one. (Superior figures are commonly used as
footnote markers.)

