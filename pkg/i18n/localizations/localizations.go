// Code generated by go-localize; DO NOT EDIT.
// This file was generated by robots at
// 2020-05-29 14:51:56.086297 &#43;0800 CST m=&#43;0.006204636

package localizations

import (
	"bytes"
	"fmt"
	"text/template"
)

var localizations = map[string]string{
	"en.messages.delete_credential_failed": "delete credential failed , credential has associated resources!",
	"en.messages.invalid_credential_name":  "invalid credential name",
	"zh.messages.delete_credential_failed": "删除秘钥失败，秘钥有关联资源!",
	"zh.messages.invalid_credential_name":  "秘钥名称错误",
}

type Replacements map[string]interface{}

type Localizer struct {
	Locale         string
	FallbackLocale string
	Localizations  map[string]string
}

func New(locale string, fallbackLocale string) *Localizer {
	t := &Localizer{Locale: locale, FallbackLocale: fallbackLocale}
	t.Localizations = localizations
	return t
}

func (t Localizer) SetLocales(locale, fallback string) Localizer {
	t.Locale = locale
	t.FallbackLocale = fallback
	return t
}

func (t Localizer) SetLocale(locale string) Localizer {
	t.Locale = locale
	return t
}

func (t Localizer) SetFallbackLocale(fallback string) Localizer {
	t.FallbackLocale = fallback
	return t
}

func (t Localizer) GetWithLocale(locale, key string, replacements ...*Replacements) string {
	str, ok := t.Localizations[t.getLocalizationKey(locale, key)]
	if !ok {
		str, ok = t.Localizations[t.getLocalizationKey(t.FallbackLocale, key)]
		if !ok {
			return key
		}
	}
	return t.replace(str, replacements...)
}

func (t Localizer) Get(key string, replacements ...*Replacements) string {
	str := t.GetWithLocale(t.Locale, key, replacements...)
	return str
}

func (t Localizer) getLocalizationKey(locale string, key string) string {
	return fmt.Sprintf("%v.%v", locale, key)
}

func (t Localizer) replace(str string, replacements ...*Replacements) string {
	b := &bytes.Buffer{}
	tmpl, err := template.New("").Parse(str)
	if err != nil {
		return str
	}

	replacementsMerge := Replacements{}
	for _, replacement := range replacements {
		for k, v := range *replacement {
			replacementsMerge[k] = v
		}
	}

	err = template.Must(tmpl, err).Execute(b, replacementsMerge)
	if err != nil {
		return str
	}
	buff := b.String()
	return buff
}
