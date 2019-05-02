Name:		texlive-cjkutils
Version:	20190327
Release:	1
Summary:	TeXLive cjkutils package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjkutils.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjkutils.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-cjkutils.bin

%description
TeXLive cjkutils package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/hbf2gf
%doc %{_mandir}/man1/bg5conv.1*
%doc %{_texmfdistdir}/doc/man/man1/bg5conv.man1.pdf
%doc %{_mandir}/man1/cef5conv.1*
%doc %{_texmfdistdir}/doc/man/man1/cef5conv.man1.pdf
%doc %{_mandir}/man1/cefconv.1*
%doc %{_texmfdistdir}/doc/man/man1/cefconv.man1.pdf
%doc %{_mandir}/man1/cefsconv.1*
%doc %{_texmfdistdir}/doc/man/man1/cefsconv.man1.pdf
%doc %{_mandir}/man1/extconv.1*
%doc %{_texmfdistdir}/doc/man/man1/extconv.man1.pdf
%doc %{_mandir}/man1/hbf2gf.1*
%doc %{_texmfdistdir}/doc/man/man1/hbf2gf.man1.pdf
%doc %{_mandir}/man1/sjisconv.1*
%doc %{_texmfdistdir}/doc/man/man1/sjisconv.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
