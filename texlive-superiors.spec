# revision 29169
# category Package
# catalog-ctan /fonts/superiors
# catalog-date 2013-02-18 23:06:04 +0100
# catalog-license lppl
# catalog-version 1.02
Name:		texlive-superiors
Version:	1.02
Release:	1
Summary:	Attach superior figures to a font family
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/superiors
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/superiors.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/superiors.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the attachment of an arbitrary superior
figures font to a font family that lacks one. (Superior figures
are commonly used as footnote markers.) Two superior figures
fonts are provided--one matching Times, the other matching
Libertine.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/superiors/sups.enc
%{_texmfdistdir}/fonts/map/dvips/superiors/superiors.map
%{_texmfdistdir}/fonts/tfm/public/superiors/libertinesups.tfm
%{_texmfdistdir}/fonts/type1/public/superiors/libertinesups.pfb
%{_texmfdistdir}/tex/latex/public/superiors/superiors.sty
%doc %{_texmfdistdir}/doc/fonts/superiors/README
%doc %{_texmfdistdir}/doc/fonts/superiors/libfoot0-crop.pdf
%doc %{_texmfdistdir}/doc/fonts/superiors/libfoot1-crop.pdf
%doc %{_texmfdistdir}/doc/fonts/superiors/stempelfoot0-crop.pdf
%doc %{_texmfdistdir}/doc/fonts/superiors/stempelfoot1-crop.pdf
%doc %{_texmfdistdir}/doc/fonts/superiors/superiors-doc.pdf
%doc %{_texmfdistdir}/doc/fonts/superiors/superiors-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
